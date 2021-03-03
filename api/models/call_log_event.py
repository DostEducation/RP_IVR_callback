from api.mixins import TimestampMixin
from api import db

class CallLogEvent(TimestampMixin, db.Model):
    __tablename__ = 'call_log_event'
    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(255))
    cid = db.Column(db.String(255))
    cid_e164 = db.Column(db.String(255))
    called_number = db.Column(db.String(255))
    event = db.Column(db.String(255))
    data = db.Column(db.String(255))
    callduration = db.Column(db.String(255))
    record_duration = db.Column(db.String(255))
    total_call_duration = db.Column(db.String(255))
    process = db.Column(db.String(255))
    status = db.Column(db.String(255))
    telco_code = db.Column(db.String(255))
    outbound_sid = db.Column(db.String(255))
    circle = db.Column(db.String(255))
    operator = db.Column(db.String(255))
    
