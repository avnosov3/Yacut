from datetime import datetime
from urllib.parse import urljoin

from settings import CUSTOM_ID, ORIGINAL, SHORT, URL
from yacut import db

BASE_URL = 'http://localhost/'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def original_to_dict(self):
        return dict(url=self.original)

    def to_dict(self):
        return dict(url=self.original, short_link=self.get_short_link())

    def from_dict(self, data):
        for field_model, field_post in ((ORIGINAL, URL), (SHORT, CUSTOM_ID)):
            if field_post in data:
                setattr(self, field_model, data[field_post])

    def get_short_link(self):
        return urljoin(BASE_URL, self.short)
