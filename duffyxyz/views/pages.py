"""Page Blueprint."""
from flask import Blueprint, render_template, abort

from duffyxyz.models import Page


pages = Blueprint('pages', __name__, template_folder='templates')


@pages.route('/404/')
def not_found():
    """Page Not Found."""
    return render_template('errors/404.html')


@pages.route('/', defaults={'page': 'index'})
@pages.route('/<page>/')
def view_page(page):
    """Render basic page."""
    try:
        page = Page('_pages/{}.md'.format(page))
        return render_template('pages/show.html', page=page)
    except IOError:
        abort(404)
