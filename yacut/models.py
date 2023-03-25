import random
import re
from datetime import datetime
from string import ascii_letters, digits

from flask import url_for

from yacut import db

WEB_UNIQUE_MESSAGE = 'Имя {} уже занято!'
SAMPLE = ascii_letters + digits
PATTERN = rf'^[{SAMPLE}]+$'
RANDOM_SHORT_LEN = 6
ORIGINAL_LEN = 4096
MAX_SHORT_LEN = 16
SHORT_ERROR = 'Не удалось сгенерировать уникальную короткую ссылку'
SHORT_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
ORIGINAL_LEN_ERROR = 'Длина оригинальной ссылки "{}" больше чем 4096'
SHORT_LEN_ERROR = 'Длина короткой ссылки "{}" больше чем 16'
API_UNIQUE_SHORT_ERROR = 'Имя "{}" уже занято.'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LEN), nullable=False)
    short = db.Column(db.String(MAX_SHORT_LEN), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def original_to_dict(self):
        return dict(url=self.original)

    def to_dict(self):
        return dict(url=self.original, short_link=self.get_short_link())

    def get_short_link(self):
        return url_for('short_url', short=self.short, _external=True)

    @staticmethod
    def get_unique_short_id(symbols=SAMPLE, length=RANDOM_SHORT_LEN):
        short_link = ''.join(random.choices(symbols, k=length))
        if not URLMap.get_urlmap_by_short(short=short_link):
            return short_link
        raise ValueError(SHORT_ERROR)

    @staticmethod
    def get_original_or_404(short):
        return URLMap.query.filter_by(short=short).first_or_404().original

    @staticmethod
    def get_urlmap_by_short(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def create(original, short, api_validation=False):
        if short in ('', None):
            short = URLMap.get_unique_short_id()
        elif api_validation:
            original_len = len(original)
            if original_len > ORIGINAL_LEN:
                raise ValueError(ORIGINAL_LEN_ERROR.format(original_len))
            short_len = len(short)
            if short_len > MAX_SHORT_LEN:
                # raise ValueError(SHORT_LEN_ERROR.format(short_len))
                raise ValueError(SHORT_MESSAGE)
            if not re.match(PATTERN, short):
                raise ValueError(SHORT_MESSAGE)
            if URLMap.get_urlmap_by_short(short):
                raise ValueError(API_UNIQUE_SHORT_ERROR.format(short))
        urlmap = URLMap(original=original, short=short)
        db.session.add(urlmap)
        db.session.commit()
        return urlmap
