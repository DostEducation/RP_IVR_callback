from api.mixins import TimestampMixin
from api import db
from flask_sqlalchemy.query import Query as BaseQuery


class CallLogEventQuery(BaseQuery):
    def call_sid_exist(self, form_data):
        return (
            self.filter(CallLogEvent.call_sid == form_data["CallSid"]).first()
            is not None
        )


class CallLogEvent(TimestampMixin, db.Model):
    query_class = CallLogEventQuery
    __tablename__ = "call_log_event"
    id = db.Column(db.Integer, primary_key=True)
    call_sid = db.Column(db.String(255))
    account_sid = db.Column(db.String(255))
    from_number = db.Column(db.String(255))
    to_number = db.Column(db.String(255))
    call_status = db.Column(db.String(255))
    direction = db.Column(db.String(255))
    parent_call_sid = db.Column(db.String(255))
    telco_code = db.Column(db.String(255))
    telco_status = db.Column(db.String(255))
    dial_time = db.Column(db.DateTime)
    pick_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.String(255))
