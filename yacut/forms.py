from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, Optional, URL, Length, Regexp


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите длинную ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Введите ссылку')
        ]
    )
    custom_id = URLField(
        'Введите короткий вариант ссылки',
        validators=[
            Optional(strip_whitespace=False),
            # URL(),
            Length(1, 16),
            Regexp(r'^\S+$', message='Короткая ссылка не должна содержать пробелы')
        ]
    )
    submit = SubmitField('Создать')