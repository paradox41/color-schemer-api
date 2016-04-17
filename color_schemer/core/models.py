from flask.ext.login import UserMixin

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

    email = db.Column(db.String(255), primary_key=True)
    google_token = db.Column(db.Text)

    def get_id(self):
        return self.email
