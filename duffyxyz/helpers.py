import os

from flask import current_app

from duffyxyz.models import Page, Post


def get_all_pages():
    """Get list of all pages."""
    pages_dir = current_app.config.get('PAGES_DIR')
    files = ['{}/{}'.format(pages_dir, e) for e in os.listdir(pages_dir)]
    pages = list()
    for f in files:
        pages.append(Page(f))
    return pages


def get_all_posts():
    """Get list of all posts."""
    posts_dir = current_app.config.get('POSTS_DIR')
    years = ['{}/{}'.format(posts_dir, e) for e in os.listdir(posts_dir)]
    unsorted_posts = list()
    for year in years:
        for post in ['{}/{}'.format(year, e) for e in os.listdir(year)]:
            unsorted_posts.append(Post(post))
    return sorted(unsorted_posts, key=lambda x: x.date, reverse=True)
