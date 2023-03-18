from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, Optional, URL


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL()
        ]
    )
    custom_id = URLField(
        'Введите короткий вариант ссылки',
        validators=[
            Optional(),
            URL()
        ]
    )
    button = SubmitField('Добавить')