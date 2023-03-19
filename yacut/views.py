import random
from urllib.parse import urlparse

from flask import render_template, flash
from sqlalchemy.exc import IntegrityError

from yacut import app, db
from .models import URLMap
from .forms import URLMapForm

SAMPLE = (
    '123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
)

SHORT_MESSAGE = 'Ваша короткая ссылка готова:'
UNIQUE_MESSAGE = 'Такой вариант короткой ссылки уже существует'


def get_unique_short_id():
    short_link = ''.join(random.choice(SAMPLE) for _ in range(random.randint(1, 6)))
    return short_link


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('main.html', form=form)
    short = get_unique_short_id() if form.custom_id.data == '' else form.custom_id.data
    original = form.original_link.data
    try:
        urlmap = URLMap(
            original=original,
            short=short,
        )
        db.session.add(urlmap)
        db.session.commit()
        flash(SHORT_MESSAGE, 'short')
        flash(urlparse(original)._replace(
            path=short, params='', query='', fragment='').geturl(),
            'short-link'
        )
    except IntegrityError:
        flash(UNIQUE_MESSAGE, 'unique')
    return render_template('main.html', form=form, urlmap=urlmap)
