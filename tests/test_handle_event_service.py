from api.services import handle_event_service
from api import models, db
from urllib.request import Request


class TestHandleEventService:
    def test_handle_event_service(self, mocker):

        # To check that methods should not be called not called when CallSid exist.
        request = Request
        request.method = "POST"
        request.url = "http://0.0.0.0:8080/?CallSid=9182161650233761&AccountSid=123456789123&From=917046650321&To=+918068971703&CallStatus=Missed&Direction=inbound-api&ParentCallSid=9182161650233761"
        request.form = {
            "CallSid": "9182161650233761",
            "AccountSid": "123456789123",
            "From": "09704665087",
            "To": "+918068971703",
            "CallStatus": "Missed",
            "Direction": "inbound-api",
            "ParentCallSid": "9182161650233761",
        }
        mocked_create_call_log_event = mocker.patch(
            "api.services.CallLogEventService.create_call_log_event", return_value=True
        )
        mocked_create_registration = mocker.patch(
            "api.services.RegistrationService.create_registration", return_value=True
        )

        handle_event_service.HandleEventService.handle_event_service(self, request)

        assert not mocked_create_call_log_event.called
        assert not mocked_create_registration.called

        # To check if the methods are called when CallSid does not exist.
        request.form = {
            "CallSid": "91821616502353761",
            "AccountSid": "123456789123",
            "From": "09704665087",
            "To": "+918068971703",
            "CallStatus": "Missed",
            "Direction": "inbound-api",
            "ParentCallSid": "9182161650233761",
        }

        handle_event_service.HandleEventService.handle_event_service(self, request)

        assert mocked_create_call_log_event.called
        assert mocked_create_registration.called
