import random
import re
from datetime import datetime

from flask import url_for

from settings import (ATTEMPTS, ORIGINAL_LEN, PATTERN, RANDOM_SHORT_LEN,
                      SAMPLE, SHORT_LEN)
from yacut import db
from yacut.error_handlers import ShortGenerateError, ValidationError

# SHORT_ERROR = 'Не удалось сгенерировать уникальную короткую ссылку'
WEB_UNIQUE_MESSAGE = 'Имя {} уже занято!'
SHORT_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
ORIGINAL_LEN_ERROR = 'Длина оригинальной ссылки "{}" больше чем 4096'
SHORT_LEN_ERROR = 'Длина короткой ссылки "{}" больше чем 16'
API_UNIQUE_SHORT_ERROR = 'Имя "{}" уже занято.'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LEN), nullable=False)
    short = db.Column(db.String(SHORT_LEN), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def original_to_dict(self):
        return dict(url=self.original)

    def to_dict(self):
        return dict(url=self.original, short_link=self.get_short_link())

    def get_short_link(self):
        return url_for('short_url', short=self.short, _external=True)

    @staticmethod
    def get_unique_short_id(symbols=SAMPLE, length=RANDOM_SHORT_LEN):
        for _ in range(ATTEMPTS):
            short_link = ''.join(random.choices(symbols, k=length))
            if not URLMap.get_urlmap_by_short(short=short_link):
                return short_link
        raise ShortGenerateError(
            WEB_UNIQUE_MESSAGE.format(short_link)
        )

    @staticmethod
    def get_original_or_404(short):
        return URLMap.query.filter_by(short=short).first_or_404().original

    @staticmethod
    def get_urlmap_by_short(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def create(original, short=None, to_validate=False):
        if not short:
            short = URLMap.get_unique_short_id()
        if to_validate:
            original_len = len(original)
            if original_len > ORIGINAL_LEN:
                raise ValidationError(ORIGINAL_LEN_ERROR.format(original_len))
            short_len = len(short)
            if short_len > SHORT_LEN:
                # raise ValueError(SHORT_LEN_ERROR.format(short_len))
                raise ValidationError(SHORT_MESSAGE)
            if not re.match(PATTERN, short):
                raise ValidationError(SHORT_MESSAGE)
            if URLMap.get_urlmap_by_short(short):
                raise ValidationError(API_UNIQUE_SHORT_ERROR.format(short))
        urlmap = URLMap(original=original, short=short)
        db.session.add(urlmap)
        db.session.commit()
        return urlmap
