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
SYMBOLS_OF_SHORT = ascii_letters + digits
VALID_SYMBOLS_OF_SHORT = (
    rf'^[{re.escape(SYMBOLS_OF_SHORT)}]+$'
)
ATTEMPTS = 3
