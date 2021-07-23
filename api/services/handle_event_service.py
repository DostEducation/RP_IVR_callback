import requests
from flask import request
from api import models, db
from . import registration_service as registration
from . import call_log_event_service as call_log_event


class HandleEventService:
    def handle_event_service(self, request):

        call_sid_exist = db.session.query(
            db.exists().where(models.CallLogEvent.call_sid == request.form["CallSid"])
        ).scalar()

        if call_sid_exist:
            return

        url_decoded_system_phone = requests.utils.unquote(request.form["To"])

        system_phone_exists = db.session.query(
            db.exists().where(models.SystemPhone.phone == url_decoded_system_phone)
        ).scalar()

        if not system_phone_exists:
            return

        try:
            data = {}
            data["call_sid"] = request.form["CallSid"]
            data["account_sid"] = request.form["AccountSid"]
            data["from_number"] = request.form["From"]
            data["to_number"] = url_decoded_system_phone
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

                """PickTime is available only when the call is answered.
                The telco code for answered calls is 16.
                """
                if request.form["TelcoCode"] == "16":
                    data["pick_time"] = request.form["PickTime"]

            call_log_event.CallLogEventService.create_call_log_event(self, data)
            if data["call_status"] == "Missed":
                registration.RegistrationService.create_registration(self, data)

        except IndexError:
            print("Failed to log the call details")
