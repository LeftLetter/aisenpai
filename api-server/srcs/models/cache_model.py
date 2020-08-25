"""キャッシュサーバであるetcdを操作するモデル"""
import json
from threading import Lock

import etcd3


class EtcdWrapper:
    """
    キャッシュサーバであるetcdを操作するモデルクラス
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        raise NotImplementedError("")

    @classmethod
    def __internal_new__(cls):
        cls._etcd = etcd3.client(host="etcd", port=2379)
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                cls._instance = cls.__internal_new__()

        return cls._instance

    def get_cache(self, key):
        """
        キャッシュを取得する
        """
        value = self._etcd.get(key)
        return value[0].decode()

    def put_cache(self, key, value):
        """
        キャッシュを追加する
        """
        jsonstring = json.dumps(value, ensure_ascii=False)
        self._etcd.put(key, jsonstring)

    def cache_exists(self, key):
        """
        キャッシュの存在判定をする
        """
        value = self._etcd.get(key)
        if value[0] is None:
            return False
        else:
            return True
