#!/usr/bin/env python
"""Management commands for Duffy.xyz."""
import os
import datetime
import frontmatter

from flask_script import Manager, prompt, prompt_bool
from slugify import slugify

from duffyxyz import app
from duffyxyz.helpers import get_all_pages, get_all_posts


manager = Manager(app)


@manager.command
def create_post():
    """Create a new post."""
    date = prompt('Date', default=datetime.datetime.now())

    title = prompt('Title')
    slug = prompt('Slug', default=slugify(title))

    post_filename = '{}/{}/{}.md'.format(
        app.config['POSTS_DIR'], date.year, slug)
    if os.path.isfile(post_filename):
        print("Existing post found with same filename!")
        if not prompt_bool("Overwrite existing post?"):
            exit('Stopping.')

    print('Creating post {}'.format(post_filename))
    post = frontmatter.Post('', date=date, title=title)

    with open(post_filename, 'w') as f:
        frontmatter.dump(post, f)


@manager.command
def freeze():
    """Generate static website."""
    from flask_frozen import Freezer
    freezer = Freezer(app)

    @freezer.register_generator
    def view_page():
        for page in get_all_pages():
            yield 'pages.view_page', {'page': page.slug}

    @freezer.register_generator
    def view_post():
        for post in get_all_posts():
            yield 'journal.view_post', {
                'post': '{}/{}'.format(post.date.year, post.slug)
            }

    @freezer.register_generator
    def not_found():
        yield "/404/"

    freezer.freeze()


if __name__ == '__main__':
    manager.run()
