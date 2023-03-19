import random

from flask import render_template, flash

from yacut import app, db
from .models import URLMap
from .forms import URLMapForm

SAMPLE = (
    '123456789'
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
)


def get_unique_short_id():
    short_link = ''.join(random.choice(SAMPLE) for _ in range(6))
    return short_link


# print(get_unique_short_id())

@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('main.html', form=form)
    short = form.custom_id.data
    print(short)
    original = form.original_link.data
    if short != '':
        urlmap = URLMap(
            original=original,
            short=short,
        )
        db.session.add(urlmap)
        db.session.commit()
    # return 'new's
        return render_template('main.html', form=form)
    db.session.add(URLMap(original=original, short=get_unique_short_id()))
    db.session.commit()
    flash(get_unique_short_id())
    return render_template('main.html', form=form)
