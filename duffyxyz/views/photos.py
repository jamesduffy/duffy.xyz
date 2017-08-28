import os
import markdown
import frontmatter
import datetime

from flask import Blueprint, render_template

# from duffyxyz.models import Photoset

photos = Blueprint('photos', __name__, template_folder='templates')


class Photoset(object):
    def __init__(self, path):
        self.path = path

        with open('{}/metadata.md'.format(self.path)) as f:
            self.metadata, self._snippet = frontmatter.parse(f.read())

        with open('{}/content.html'.format(self.path)) as f:
            self._content = f.read()

    @property
    def html(self):
        return unicode(self._content, "utf-8")

    @property
    def title(self):
        return self.metadata.get('title', None)

    @property
    def slug(self):
        return self.path.split('/')[-1]

    @property
    def snippet(self):
        return markdown.markdown(self._snippet)

    @property
    def date(self):
        if 'date' not in self.metadata:
            return None
        d = self.metadata.get('date')
        if isinstance(d, datetime.date):
            d = datetime.datetime.combine(d, datetime.datetime.min.time())
        return d


def get_all_photosets():
    photoset_dir = current_app.config.get('PHOTOS_DIR')
    files = ['{}/{}'.format(photoset_dir, e) for e in os.listdir(photoset_dir)]
    unsorted_posts = list()
    for f in files:
        unsorted_posts.append(Photoset(f))
    return sorted(unsorted_posts, key=lambda x: x.date, reverse=True)


@photos.route('/')
def index():
    return render_template('photos/list.html', photosets=get_all_photosets())


@photos.route('/set/<slug>')
def set(slug):
    photoset = Photoset('{}/{}'.format(current_app.config.get('PHOTOS_DIR'), slug))
    return render_template('photos/photoset.html', photoset=photoset)
