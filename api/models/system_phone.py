from api.mixins import TimestampMixin
from api import db
from flask_sqlalchemy.query import Query as BaseQuery


class SystemPhoneQuery(BaseQuery):
    def system_phone_exists(self, url_decoded_system_phone):
        return (
            self.filter(
                SystemPhone.phone.contains(url_decoded_system_phone[-10:])
            ).first()
            is not None
        )


class SystemPhone(TimestampMixin, db.Model):
    query_class = SystemPhoneQuery
    __tablename__ = "system_phone"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(50))
    district = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(255))
