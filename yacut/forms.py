from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

NOT_SPACE_PATTERN = r'^\S+$'

URL_MESSAGE = 'Проверьте формат ссылки'
SPACE_MESSAGE = 'Короткая ссылка не должна содержать пробелы'
REQUIRED_FIELD_MESSAGE = 'Обязательное поле'


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите длинную ссылку',
        validators=[
            DataRequired(message=REQUIRED_FIELD_MESSAGE),
            URL(message=URL_MESSAGE)
        ]
    )
    custom_id = URLField(
        'Введите короткий вариант ссылки',
        validators=[
            Optional(strip_whitespace=False),
            Length(1, 16),
            Regexp(NOT_SPACE_PATTERN, message=SPACE_MESSAGE)
        ]
    )
    submit = SubmitField('Создать')