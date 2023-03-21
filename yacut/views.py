import random

from flask import flash, redirect, render_template
from sqlalchemy.exc import IntegrityError

from settings import SHORT, SHORT_LINK, UNIQUE
from yacut import app, db
from .forms import URLMapForm
from .models import URLMap

SAMPLE = (
    '123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
)

SHORT_MESSAGE = 'Ваша короткая ссылка готова:'
WEB_UNIQUE_MESSAGE = 'Имя {} уже занято!'


def get_unique_short_id():
    short_link = ''.join(random.choice(SAMPLE) for _ in range(6))
    return short_link


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('main.html', form=form)
    short = get_unique_short_id() if form.custom_id.data in ('', None) else form.custom_id.data
    original = form.original_link.data
    try:
        urlmap = URLMap(
            original=original,
            short=short,
        )
        db.session.add(urlmap)
        db.session.commit()
        flash(SHORT_MESSAGE, SHORT)
        flash(
            urlmap.get_short_link(),
            SHORT_LINK
        )
    except IntegrityError:
        flash(WEB_UNIQUE_MESSAGE.format(short), UNIQUE)
    return render_template('main.html', form=form, urlmap=urlmap)


@app.route('/<string:short>')
def short_url(short):
    return redirect(URLMap.query.filter_by(short=short).first_or_404().original)
