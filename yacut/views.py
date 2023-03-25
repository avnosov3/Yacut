from flask import redirect, render_template

from yacut import app
from .forms import URLMapForm
from .models import URLMap

SHORT_MESSAGE = 'Ваша короткая ссылка готова:'
WEB_UNIQUE_MESSAGE = 'Имя {} уже занято!'


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    original = form.original_link.data
    short = form.data.get('custom_id') or None
    return render_template(
        'index.html', form=form,
        urlmap=URLMap.create(original=original, short=short))


@app.route('/<string:short>')
def short_url(short):
    return redirect(URLMap.get_original_or_404(short))
