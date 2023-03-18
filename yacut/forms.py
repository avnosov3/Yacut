from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, Optional, URL, Length


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите длинную ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL()
        ]
    )
    custom_id = URLField(
        'Введите короткий вариант ссылки',
        validators=[
            Optional(),
            # URL(),
            Length(1, 16)
        ]
    )
    submit = SubmitField('Создать')