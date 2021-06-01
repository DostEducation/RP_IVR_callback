from api.mixins import TimestampMixin
from api import db


class Partner(TimestampMixin, db.Model):
    __tablename__ = "partner"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
