"""duffy.xyz base config."""
import os


DEBUG = True
SECRET_KEY = 'CONFIG_SECREY_KEY'

BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')

FREEZER_BASE_URL = 'https://duffy.xyz'
FREEZER_DESTINATION = os.path.join(BASE_DIR, 'build')
FREEZER_REMOVE_EXTRA_FILES = True

POSTS_DIR = os.path.join(BASE_DIR, '_posts')
PAGES_DIR = os.path.join(BASE_DIR, '_pages')
PHOTOS_DIR = os.path.join(BASE_DIR, '_photosets')

TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')
