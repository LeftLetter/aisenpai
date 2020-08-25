"""関連語を導出するモデル"""
from pathlib import Path
from threading import Lock

from flask import current_app
from gensim.models.fasttext import FastText


class FasttextWrapper:
    """
    関連語を導出するモデルクラス
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        raise NotImplementedError("")

    @classmethod
    def __internal_new__(cls):
        cls._model_path = str(
            Path(str(current_app.root_path)) / "resources/fasttext_model/ft_sg.model"
        )
        cls._sg_model = FastText.load(cls._model_path)
        cls._logger = current_app.logger

        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                cls._instance = cls.__internal_new__()

        return cls._instance

    def get_similar_words(self, word):
        """
        関連語を導出する
        """
        try:
            word_list = self._sg_model.wv.most_similar(positive=[word])
            return word_list
        except Exception as error:
            self._logger.error(error)
            return []
