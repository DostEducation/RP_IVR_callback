from api.services import call_log_event_service, registration_service
from api import models
from unittest.mock import Mock

# from services import


class TestCreateRegistartion:
    def test_create_registration(self, mocker):

        data = {
            "call_sid": "9182161650233761",
            "account_sid": "123456789123",
            "from_number": "09704657665087",
            "to_number": "+918068971703",
            "call_status": "Missed",
            "direction": "inbound-api",
            "parent_call_sid": "9182161650233761",
            "telco_code": None,
            "telco_status": None,
            "dial_time": None,
            "pick_time": None,
            "end_time": None,
            "duration": None,
        }

        # system_phone_data = models.SystemPhone.query.filter_by(
        #     phone=data["to_number"]
        # ).first()

        # partner = models.PartnerSystemPhone.query.filter_by(
        #     system_phone_id=system_phone_data.id
        # ).first()

        registration = models.Registration(
            user_phone=data["from_number"],
            system_phone=data["to_number"],
            status="pending",
            partner_id=1,
            state="UP",
            has_dropped_missedcall=True,
        )

        mocked_add = mocker.patch("api.db.session.add", return_value=True)
        mocked_commit = mocker.patch("api.db.session.commit", return_value=True)

        registration_service.RegistrationService.create_registration(self, data)

        assert mocked_add.called
        assert mocked_commit.called
