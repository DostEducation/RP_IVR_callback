# This file is treated as service layer
from flask import request
from api import helpers, models, db
from datetime import datetime
import logging, traceback


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
            created_on=data["log_created_on"]
            if data.get("log_created_on", None)
            else datetime.now(),
        )
        try:
            helpers.save(call_log_event)
            logging.info("Call Log Event saved successfully.")
        except Exception as e:
            logging.error("Error occurred while saving Call Log Event: " + str(e))
            print(traceback.format_exc())
            logging.warning("Rolling back the transaction.")
