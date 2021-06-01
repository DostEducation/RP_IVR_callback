from api.mixins import TimestampMixin
from api import db


class Program(TimestampMixin, db.Model):
    __tablename__ = "program"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255), nullable=True)
