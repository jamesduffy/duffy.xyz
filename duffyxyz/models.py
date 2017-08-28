import markdown
import frontmatter
import datetime


class Entry(object):
    def __init__(self, path):
        self.path = path

        with open(self.path) as f:
            self.metadata, self.content = frontmatter.parse(f.read())

    @property
    def html(self):
        return markdown.markdown(self.content)

    @property
    def title(self):
        return self.metadata.get('title', None)

    @property
    def featured_image(self):
        return self.metadata.get('featured-image', None)

    @property
    def snippet(self):
        if self.metadata.get('snippet'):
            return self.metadata.get('snippet')
        else:
            return self.content[:120] + (self.content[120:] and '...')

    @property
    def slug(self):
        return self.path.split('/')[-1][:-3]


class Page(Entry):
    pass


class Post(Entry):
    def __init__(self, path):
        self.path = path

        with open(self.path) as f:
            self.metadata, self.content = frontmatter.parse(f.read())

    @property
    def date(self):
        if 'date' not in self.metadata:
            return None
        d = self.metadata.get('date')
        if isinstance(d, datetime.date):
            d = datetime.datetime.combine(d, datetime.datetime.min.time())
        return d


# class Photoset(object):
#     pass
    # def __init__(self, path):
    #     self.path = path

    #     with open(self.path) as f:
    #         self.metadata, self.content - frontmatter()
