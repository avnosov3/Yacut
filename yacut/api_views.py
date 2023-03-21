import re

from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from settings import CUSTOM_ID, URL
from yacut import app, db
from .error_handlers import InvalidAPIUsage
from .forms import NOT_SPACE_PATTERN, URL_MESSAGE
from .models import URLMap
from .views import get_unique_short_id

NOT_SPACE_PATTERN_SHORT = r'^[a-zA-Z0-9]{1,16}$'
URL_PATTERN = (
    r"^[a-z]+://"
    r"(?P<host>[^\/\?:]+)"
    r"(?P<port>:[0-9]+)?"
    r"(?P<path>\/.*?)?"
    r"(?P<query>\?.*)?$"
)

NOT_FOUND_MESSAGE = 'Указанный id не найден'
EMPTY_MESSAGE = 'Отсутствует тело запроса'
EMPTY_URL_MESSAGE = '"url" является обязательным полем!'
SHORT_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
API_UNIQUE_MESSAGE = 'Имя "{}" уже занято.'


@app.route('/api/id/<string:short_id>/')
def get_original_link(short_id):
    original = URLMap.query.filter_by(short=short_id).first()
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
    url = data[URL]
    data[CUSTOM_ID] = get_unique_short_id() if CUSTOM_ID not in data or data[CUSTOM_ID] in ('', None) else data[CUSTOM_ID]
    CASES = (
        (NOT_SPACE_PATTERN, url, EMPTY_URL_MESSAGE),
        (URL_PATTERN, url, URL_MESSAGE),
        (NOT_SPACE_PATTERN_SHORT, data[CUSTOM_ID], SHORT_MESSAGE)
    )
    for pattern, link, message in CASES:
        if not re.match(pattern, link):
            raise InvalidAPIUsage(message, 400)
    try:
        urlmap = URLMap()
        urlmap.from_dict(data)
        db.session.add(urlmap)
        db.session.commit()
    except IntegrityError:
        raise InvalidAPIUsage(API_UNIQUE_MESSAGE.format(data[CUSTOM_ID]), 400)
    return jsonify(urlmap.to_dict()), 201
