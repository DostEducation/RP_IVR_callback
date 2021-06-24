from api.services import call_log_event_service
from api import models


class TestCreateCallLogEvent:
    def test_create_call_log_event(self, mocker):

        data = {
            "call_sid": "9182161650233761",
            "account_sid": "123456789123",
            "from_number": "0970467665087",
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

        mocked_add = mocker.patch("api.db.session.add", return_value=True)
        mocked_commit = mocker.patch("api.db.session.commit", return_value=True)

        call_log_event_service.CallLogEventService.create_call_log_event(self, data)

        assert mocked_add.called
        assert mocked_commit.called
