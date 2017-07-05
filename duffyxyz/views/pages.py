from flask import Blueprint, render_template, abort

from duffyxyz.models import Page


pages = Blueprint('pages', __name__, template_folder='templates')


@pages.route('/', defaults={'page': 'index'})
@pages.route('/<page>')
def show(page):
    try:
        print('looking for page {}'.format(page))
        page = Page('_pages/{}.md'.format(page))
        return render_template('pages/show.html', page=page)
    except IOError:
        abort(404)
