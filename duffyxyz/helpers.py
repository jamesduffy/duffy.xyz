import os

from flask import current_app

from duffyxyz.models import Post


def get_all_posts():
    posts_dir = current_app.config.get('POSTS_DIR')
    files = ['{}/{}'.format(posts_dir, e) for e in os.listdir(posts_dir)]
    unsorted_posts = list()
    for f in files:
        unsorted_posts.append(Post(f))
    return sorted(unsorted_posts, key=lambda x: x.date, reverse=True)
