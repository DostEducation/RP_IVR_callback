import requests
from flask import request
from api import models, db, app
from . import registration_service as registration
from . import call_log_event_service as call_log_event


class HandleEventService:
    def handle_event_service(self, form_data):
        call_sid_exist = db.session.query(
            db.exists().where(models.CallLogEvent.call_sid == form_data["CallSid"])
        ).scalar()

        if call_sid_exist:
            return

        url_decoded_system_phone = requests.utils.unquote(form_data["To"])

        system_phone_exists = db.session.query(
            db.exists().where(models.SystemPhone.phone == url_decoded_system_phone)
        ).scalar()

        if not system_phone_exists:
            return

        # try:
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
                data["pick_time"] = form_data["PickTime"]

        call_log_event.CallLogEventService.create_call_log_event(self, data)
        if data["call_status"] == "Missed":
            registration.RegistrationService.create_registration(self, data)

        # except IndexError:
            # print("Failed to log the call details")
