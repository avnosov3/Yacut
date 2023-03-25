from flask import jsonify, request

from settings import CUSTOM_ID, URL
from yacut import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap

NOT_FOUND_MESSAGE = 'Указанный id не найден'
EMPTY_MESSAGE = 'Отсутствует тело запроса'
EMPTY_URL_MESSAGE = '"url" является обязательным полем!'
SHORT_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
API_UNIQUE_MESSAGE = 'Имя "{}" уже занято.'


@app.route('/api/id/<string:short_id>/')
def get_original_link(short_id):
    original = URLMap.get_urlmap_by_short(short=short_id)
    if original is None:
        raise InvalidAPIUsage(NOT_FOUND_MESSAGE, 404)
    return jsonify(original.original_to_dict()), 200


@app.route('/api/id/', methods=['POST'])
def generate_link():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage(EMPTY_MESSAGE, 400)
    if URL not in data:
        raise InvalidAPIUsage(EMPTY_URL_MESSAGE, 400)
    try:
        urlmap = URLMap.create(
            data[URL], data.get(CUSTOM_ID), api_validation=True
        )
    except ValueError as error:
        raise InvalidAPIUsage(str(error))
    return jsonify(urlmap.to_dict()), 201
