"""Post blueprint."""
from flask import Blueprint, render_template, abort, current_app

from duffyxyz.helpers import get_all_posts
from duffyxyz.models import Post


blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/')
def index():
    """Post list."""
    return render_template('blog/index.html', posts=get_all_posts())


@blog.route('/<path:post>/')
def view_post(post):
    """Single post."""
    try:
        post = Post('{}/{}.md'.format(current_app.config.get('POSTS_DIR'), post))
        return render_template('blog/post.html', post=post)
    except IOError:
        abort(404)
