# This file is treated as service layer
from flask import request
from api import models, db


class CallLogEventService:
    # Create a call log event
    def create_call_log_event(self, data):
        call_log_event = models.CallLogEvent(
            call_sid=data["call_sid"],
            account_sid=data["account_sid"],
            from_number=data["from_number"],
            to_number=data["to_number"],
            call_status=data["call_status"],
            direction=data["direction"],
            parent_call_sid=data["parent_call_sid"],
            telco_code=data["telco_code"],
            telco_status=data["telco_status"],
            dial_time=data["dial_time"],
            pick_time=data["pick_time"],
            end_time=data["end_time"],
            duration=data["duration"],
        )
        db.session.add(call_log_event)
        db.session.commit()
