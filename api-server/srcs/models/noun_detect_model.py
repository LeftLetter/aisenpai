"""テキストの中からQiitaのタグに含まれる名詞を抜き出すモデル"""
import json
from pathlib import Path
from threading import Lock

import spacy
from flask import current_app


class GinzaWrapper:
    """
    テキストの中からQiitaのタグに含まれる名詞を抜き出すモデルクラス
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        raise NotImplementedError("")

    @classmethod
    def __internal_new__(cls):
        cls._nlp = spacy.load("ja_ginza")
        cls._dic_path = (
            Path(str(current_app.root_path)) / "resources/tags/qiita_tag.json"
        )
        cls._tags = json.load(open(cls._dic_path))
        cls._logger = current_app.logger

        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                cls._instance = cls.__internal_new__()

        return cls._instance

    def get_noun(self, sentence):
        """
        テキストの中からQiitaのタグに含まれる名詞を抜き出す
        """
        try:
            doc = self._nlp(sentence)
            # 名詞抜き出し
            nouns = []
            for sent in doc.sents:
                nouns += filter(lambda e: e.pos_ == "NOUN", sent)
            nouns = list(map(lambda e: e.orth_, nouns))
            # タグに含まれる名詞のみ返却
            results = []
            for noun in nouns:
                for tag in self._tags:
                    if noun == tag["id"]:
                        results.append(noun)

            return results
        except Exception as error:
            self._logger.error(error)
            return []
