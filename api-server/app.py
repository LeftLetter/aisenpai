from flask import Flask, request, jsonify
from flask.logging import create_logger
import json
from distutils.util import strtobool
from modules.text_summarization.text_summarization import LexRank
from modules.sentence_embedding.sentence_embedding import BertWrapper
from modules.noun_detector.noun_detector import MecabWrapper
from modules.word_embedding.word_embedding import fastTextWrapper
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
logger = create_logger(app)


# 入力文章に似た文章の獲得
@app.route('/sentence', methods=['GET'])
def get_similar_sentence():
    logger.info('start /sentence')
    response = {
        'title': 'mock_title'
    }
    return jsonify(response)
    # try:
    #     sentence = request.args.get('sentence')

    #     # BERTで似たタイトルの文章を取得
    #     similar_sentence = BertWrapper().get_similar_sentence(sentence)
    #     response = {
    #         'title': similar_sentence['title']
    #     }

    #     logger.info('finish /sentence')
    #     return jsonify(response)
    # except Exception as e:
    #     logger.error(e)
    #     logger.info('finish /sentence')
    #     return jsonify({
    #         'error': 'error'
    #     })


# 入力文章を要約
@app.route('/summary', methods=['GET'])
def get_summary():
    logger.info('start /summary')
    sentence = request.args.get('sentence')
    response = {
        'body': sentence
    }
    return jsonify(response)
    # try:
    #     sentence = request.args.get('sentence')
    #     # count = request.args.get('count')

    #     # LexRankで要約
    #     summarized_article = LexRank().lexrank_from_string(sentence)
    #     response = {
    #         'body': summarized_article
    #     }

    #     logger.info('finish /summary')
    #     return jsonify(response)
    # except Exception as e:
    #     logger.error(e)
    #     logger.info('finish /summary')
    #     return jsonify({
    #         'error': 'error'
    #     })

# 入力文章中の名詞に似た単語の獲得
@app.route('/word', methods=['GET'])
def get_similar_words():
    logger.info('start /word')
    response = {
        'words': ['a', 'b', 'c']
    }
    return jsonify(response)
    # try:
    #     sentence = request.args.get('sentence')
    #     use_dic = strtobool(request.args.get('useDictionary'))
    #     # model = request.args.get('model')
    #     # corpus = request.args.get('corpus')

    #     # Mecabによる名詞抽出
    #     noun_list = MecabWrapper().get_noun(sentence, use_dic)
    #     response = {
    #         'words': []
    #     }

    #     # fastTextで意味の近い単語を抽出
    #     ft = fastTextWrapper()
    #     for noun in noun_list:
    #         if noun != '*':
    #             similar_words = ft.get_similar_words(noun.lower())
    #             record = {'keyword': noun, 'similarWords': []}
    #             for similar_word in similar_words:
    #                 print(similar_word)
    #                 record['similarWords'].append(
    #                     {'word': similar_word[0], 'value': similar_word[1]})
    #             response['words'].append(record)

    #     logger.info('finish /word')
    #     return jsonify(response)
    # except Exception as e:
    #     logger.error(e)
    #     logger.info('finish /word')
    #     return jsonify({
    #         'error': 'error'
    #     })

# Qiita
@app.route('/qiita', methods=['GET'])
def search_qiita_article():
    # headers = {
    #     'Authorization': 'Bearer'
    # }

    # params = {
    #     'page': 1,
    #     'query': 'title:' + request.args.get('sentence')
    # }

    # res = requests.get('https://qiita.com/api/v2/items',
    #                    params=params, headers=headers, verify=False)

    # res = res.json()
    # soup = BeautifulSoup(res[0]['rendered_body'], 'html.parser')
    # sentences = soup.find_all('p')
    # text = ''
    # for sentence in sentences:
    #     text += sentence.text + '\n'
    # res[0]['rendered_body'] = text

    return jsonify({'body': 'mock_content'})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
