# This file is treated as service layer
from api import helpers, models
from datetime import datetime
from utils.loggingutils import logger
import traceback


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
        except Exception as e:
            logger.error(
                f"Error occurred while saving Call Log Event for user phone {call_log_event.from_number}: {e}"
            )
            logger.debug(traceback.format_exc())
