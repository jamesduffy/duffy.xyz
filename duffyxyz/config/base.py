"""duffy.xyz base config"""
import os


DEBUG = False
SECRET_KEY = 'BASE_CONFIG_SECREY_KEY'

BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')

POSTS_DIR = os.path.join(BASE_DIR, '_posts')
PAGES_DIR = os.path.join(BASE_DIR, '_pages')
PHOTOS_DIR = os.path.join(BASE_DIR, '_photosets')
