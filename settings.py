import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET_KEY')


ORIGINAL = 'original'
SHORT = 'short'
SHORT_LINK = 'short-link'
UNIQUE = 'unique'
URL = 'url'
CUSTOM_ID = 'custom_id'