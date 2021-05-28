from api.mixins import TimestampMixin
from api import db


class Program(TimestampMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    address_line_1 = db.Column(db.Text, nullable=True)
    address_line_2 = db.Column(db.Text, nullable=True)
    postal_code = db.Column(db.String(50), nullable=True)
    partner_id = db.Column(db.Integer)
    city = db.Column(db.String(100), nullable=True)
    district = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(50), nullable=True)
    partner = db.Column(db.Integer, db.ForeignKey("partner.id", ondelete="CASCADE"))
