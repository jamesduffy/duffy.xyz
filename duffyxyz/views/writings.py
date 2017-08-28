"""Post blueprint."""
from flask import Blueprint, render_template, abort, current_app

from duffyxyz.helpers import get_all_posts
from duffyxyz.models import Post


writings = Blueprint('writings', __name__, template_folder='templates')


@writings.route('/')
def index():
    """Post list."""
    return render_template('writings/index.html', posts=get_all_posts())


@writings.route('/<path:post>/')
def view_post(post):
    """Single post."""
    try:
        post = Post('{}/{}.md'.format(current_app.config.get('POSTS_DIR'), post))
        return render_template('writings/post.html', post=post)
    except IOError:
        abort(404)
