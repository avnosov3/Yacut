import os
import re
from string import ascii_letters, digits


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'ART')


ORIGINAL_LEN = 4096
SHORT_LEN = 16
RANDOM_SHORT_LEN = 6
SAMPLE = ascii_letters + digits
PATTERN = rf'^[{re.escape(SAMPLE)}]+$'
ATTEMPTS = 3
