import requests
from api import models, app
from . import user_service as user
from . import registration_service as registration
from . import call_log_event_service as call_log_event
from utils.loggingutils import logger
import traceback


class HandleEventService:
    def handle_event_service(self, form_data):
        call_sid_exist = models.CallLogEvent.query.call_sid_exist(form_data)

        if call_sid_exist:
            return

        url_decoded_system_phone = requests.utils.unquote(form_data["To"])

        system_phone_exists = models.SystemPhone.query.system_phone_exists(
            url_decoded_system_phone
        )

        if not system_phone_exists:
            return

        try:
            data = {}
            data["call_sid"] = form_data["CallSid"]
            data["account_sid"] = form_data["AccountSid"]
            data["from_number"] = form_data["From"]
            data["to_number"] = url_decoded_system_phone
            data["call_status"] = form_data["CallStatus"]
            data["direction"] = form_data["Direction"]
            data["parent_call_sid"] = form_data["ParentCallSid"]

            data["telco_code"] = None
            data["telco_status"] = None
            data["dial_time"] = None
            data["pick_time"] = None
            data["end_time"] = None
            data["duration"] = None

            if form_data.get("log_created_on", None):
                data["log_created_on"] = form_data["log_created_on"]

            if data["call_status"] != "Missed":
                data["telco_code"] = form_data["TelcoCode"]
                data["telco_status"] = form_data["TelcoStatus"]
                data["dial_time"] = form_data["DialTime"]
                data["end_time"] = form_data["EndTime"]
                data["duration"] = form_data["Duration"]

                """PickTime is available only when the call is answered.
                The telco code for answered calls is 16.
                """
                if form_data["TelcoCode"] == str(app.config["TELCO_CODE_ANSWERED"]):
                    data["pick_time"] = form_data.get("PickTime")

            call_log_event.CallLogEventService.create_call_log_event(self, data)
            if data["call_status"] == "Missed":
                user.UserService.handle_user_creation(self, data)
                registration.RegistrationService.create_registration(self, data)

        except Exception as e:
            logger.error(
                f"Failed to log the call details for user phone {data['from_number']}: {str(e)}"
            )
            logger.debug(traceback.format_exc())
