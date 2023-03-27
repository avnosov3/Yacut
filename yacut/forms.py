from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import (
    URL, DataRequired, Length, Optional, Regexp, ValidationError
)

from settings import ORIGINAL_LEN, SHORT_LEN, VALID_SYMBOLS_OF_SHORT
from yacut.models import WEB_UNIQUE_MESSAGE, URLMap

URL_MESSAGE = 'Проверьте формат ссылки'
SPACE_MESSAGE = 'Проверьте формат короткой ссылки'
REQUIRED_FIELD_MESSAGE = 'Обязательное поле'
ORIGINAL_LINK_MESSAGE = 'Введите длинную ссылку'
CUSTOM_ID_MESSAGE = 'Введите короткий вариант ссылки'
SUMBIT_MESSAGE = 'Создать'
ORIGINAL_LEN_MESSAGE = f'Размер ссылки должен быть меньше {ORIGINAL_LEN}'
SHORT_LEN_MESSAGE = f'Размер короткой ссылки должен быть меньше {SHORT_LEN}'


class URLMapForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_LINK_MESSAGE,
        validators=[
            DataRequired(message=REQUIRED_FIELD_MESSAGE),
            URL(message=URL_MESSAGE),
            Length(max=ORIGINAL_LEN, message=ORIGINAL_LEN_MESSAGE)
        ]
    )
    custom_id = URLField(
        CUSTOM_ID_MESSAGE,
        validators=[
            Optional(strip_whitespace=False),
            Length(max=SHORT_LEN, message=SHORT_LEN_MESSAGE),
            Regexp(VALID_SYMBOLS_OF_SHORT, message=SPACE_MESSAGE)
        ]
    )
    submit = SubmitField(SUMBIT_MESSAGE)

    def validate_custom_id(self, field):
        if field.data and URLMap.get_urlmap_by_short(field.data):
            raise ValidationError(WEB_UNIQUE_MESSAGE.format(field.data))
