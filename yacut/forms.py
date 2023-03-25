from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import (URL, DataRequired, Length, Optional, Regexp,
                                ValidationError)

from yacut.models import MAX_SHORT_LEN, ORIGINAL_LEN, PATTERN, URLMap

URL_MESSAGE = 'Проверьте формат ссылки'
SPACE_MESSAGE = 'Короткая ссылка не должна содержать пробелы'
REQUIRED_FIELD_MESSAGE = 'Обязательное поле'
ORIGINAL_LINK_MESSAGE = 'Введите длинную ссылку'
CUSTOM_ID_MESSAGE = 'Введите короткий вариант ссылки'
SUMBIT_MESSAGE = 'Создать'
WEB_UNIQUE_MESSAGE = 'Имя {} уже занято!'


class URLMapForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_LINK_MESSAGE,
        validators=[
            DataRequired(message=REQUIRED_FIELD_MESSAGE),
            URL(message=URL_MESSAGE),
            Length(max=ORIGINAL_LEN)
        ]
    )
    custom_id = URLField(
        CUSTOM_ID_MESSAGE,
        validators=[
            Optional(strip_whitespace=False),
            Length(max=MAX_SHORT_LEN),
            Regexp(PATTERN, message=SPACE_MESSAGE)
        ]
    )
    submit = SubmitField(SUMBIT_MESSAGE)

    def validate_custom_id(self, field):
        if field.data and URLMap.get_urlmap_by_short(field.data):
            raise ValidationError(WEB_UNIQUE_MESSAGE.format(field.data))
