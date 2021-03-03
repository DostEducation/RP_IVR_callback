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


# -- Sequence and defined type
# CREATE SEQUENCE IF NOT EXISTS call_log_event_id_seq;

# -- Table Definition
# CREATE TABLE "public"."call_log_event" (
#     "id" int4 NOT NULL DEFAULT nextval('call_log_id_seq'::regclass),
#     "sid" varchar(255),
#     "cid" varchar(255),
#     "cid_e164" varchar(255),
#     "called_number" varchar(255),
#     "event" varchar(255),
#     "data" varchar(255),
#     "callduration" varchar(255),
#     "record_duration" varchar(255),
#     "total_call_duration" varchar(255),
#     "process" varchar(255),
#     "status" varchar(255),
#     "telco_code" varchar(255),
#     "outbound_sid" varchar(255),
#     "circle" varchar(255),
#     "operator" varchar(255),
#     PRIMARY KEY ("id")
# );
