"""元の質問と関連語を使用して記事を検索するコントローラ"""
from flask import Blueprint, current_app, jsonify, request

from ..models.article_search_model import QiitaModel

app = Blueprint("synonym", __name__)


@app.route("/api/v1/article")
def get_synonym():
    """
    元の質問と関連語を使用して記事を検索するコントローラ
    """
    qiita_model = QiitaModel.get_instance()
    logger = current_app.logger
    response = {"articles": []}
    try:
        logger.info("start article")
        # sentence = request.args.get("sentence")
        words = request.args.get("words")

        response = qiita_model.search_qiita_article(words)

        return jsonify(response)

    except Exception as error:
        logger.error(error)
        logger.info("finish article")
        return jsonify({"error": "error"})
