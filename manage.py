#!/usr/bin/env python
import os
import datetime
import frontmatter

from flask_script import Manager, prompt, prompt_bool
from slugify import slugify

from duffyxyz import app


manager = Manager(app)


@manager.command
def create_post():
    """Create a new post."""
    title = prompt('Title')
    slug = prompt('Slug', default=slugify(title))

    post_filename = '{}/{}.md'.format(app.config['POSTS_DIR'], slug)
    if os.path.isfile(post_filename):
        print("Existing post found with same filename!")
        if not prompt_bool("Overwrite existing post?"):
            exit('Stopping.')

    date = prompt('Date', default=datetime.datetime.now())
    layout = prompt('Layout', default='post')

    print('Creating post {}'.format(post_filename))
    post = frontmatter.Post('', date=date, title=title, layout=layout)

    with open(post_filename, 'w') as f:
        frontmatter.dump(post, f)


if __name__ == '__main__':
    manager.run()
