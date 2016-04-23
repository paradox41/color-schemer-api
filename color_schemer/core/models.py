from flask.ext.login import UserMixin

from sqlalchemy.dialects.postgresql import JSONB

from color_schemer import db
from color_schemer.utils import utcnow


class TimestampMixin(object):
    created_at = db.Column(
        db.DateTime(
            timezone=True),
        server_default=db.func.now(),
        default=utcnow)
    updated_at = db.Column(
        db.DateTime(
            timezone=True),
        server_default=db.func.now(),
        server_onupdate=db.func.now(),
        default=utcnow,
        onupdate=utcnow)


class User(db.Model, UserMixin, TimestampMixin):

    __tablename__ = 'users'

    email = db.Column(db.Text, primary_key=True)
    google_token = db.Column(db.Text)

    def get_id(self):
        return self.email


class Theme(db.Model, TimestampMixin):

    __tablename__ = 'themes'

    theme_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    schema = db.Column(JSONB, nullable=False, server_default='{}', default={})
    image_url = db.Column(db.Text)
    author = db.Column(db.Text, db.ForeignKey('users.email'), nullable=False)
