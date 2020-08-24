"""記事を検索するモデル"""
import os
from threading import Lock

import requests
from bs4 import BeautifulSoup
from flask import current_app


class QiitaModel:
    """
    Qiita APIで記事を検索するモデルクラス
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        raise NotImplementedError("")

    @classmethod
    def __internal_new__(cls):
        cls._headers = {"Authorization": f"Bearer {os.environ['QIITA_TOKEN']}"}
        cls._logger = current_app.logger
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                cls._instance = cls.__internal_new__()

        return cls._instance

    def search_qiita_article(self, words):
        """
        Qiita APIで記事を検索する
        """
        try:
            results = []
            for word in words:
                params = {"page": 1, "query": f"title:{word}"}
                res = requests.get(
                    "https://qiita.com/api/v2/items",
                    params=params,
                    headers=self._headers,
                )

                # 記事部分抜き出し
                res = res.json()
                soup = BeautifulSoup(res[0]["rendered_body"], "html.parser")
                sentences = soup.find_all("p")
                text = ""
                for sentence in sentences:
                    text += sentence.text + "\n"
                res[0]["rendered_body"] = text
                results.append(res[0])

            return results
        except Exception as error:
            self._logger.error(error)
            return []
