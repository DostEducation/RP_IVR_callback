# This file is treated as service layer
from flask import request
from api import models, db


class CallLogEventService:
    def handle_call_log_event(self, request):
        try:
            data = {}
            data["call_sid"] = request.form["CallSid"]
            data["account_sid"] = request.form["AccountSid"]
            data["from_number"] = request.form["From"]
            data["to_number"] = request.form["To"]
            data["call_status"] = request.form["CallStatus"]
            data["direction"] = request.form["Direction"]
            data["parent_call_sid"] = request.form["ParentCallSid"]

            data["telco_code"] = None
            data["telco_status"] = None
            data["dial_time"] = None
            data["pick_time"] = None
            data["end_time"] = None
            data["duration"] = None

            if data["call_status"] != "Missed":
                data["telco_code"] = request.form["TelcoCode"]
                data["telco_status"] = request.form["TelcoStatus"]
                data["dial_time"] = request.form["DialTime"]
                data["end_time"] = request.form["EndTime"]
                data["duration"] = request.form["Duration"]

                if (
                    (data["call_status"] != "NoAnswer")
                    and (data["call_status"] != "MaxDialTimeExceeded")
                    and (data["call_status"] != "NetworkOutOfOrder")
                    and (data["call_status"] != "Busy")
                    and (data["call_status"] != " Rejected")
                    and (data["call_status"] != " NormalUnspecified")
                    and (data["call_status"] != " RecoveryTimerOnExpiry")
                    and (data["call_status"] != " InvalidNumber")
                ):
                    data["pick_time"] = request.form["PickTime"]

            print("call sid received:")
            print(data["call_sid"])

            self.create_call_log_event(data)

        except IndexError:
            print("Failed to log the call details")

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
