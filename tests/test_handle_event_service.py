from api.services import handle_event_service
from api import models, db
from tests import mocked_request


class TestHandleEventService:
    # To check that methods should not be called not called when CallSid exist.
    def test_handle_event_service_if_call_sid_exist(self, mocker):
        request = mocked_request.mocked_request(self)

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
    def test_handle_event_service_if_call_sid_does_not_exist(self, mocker):
        request = mocked_request.mocked_request(self)
        mocked_query = db.session.query
        request.form["CallSid"] = "9182161657802353761"
        if request.form["CallSid"] == "9182161657802353761":
            mocked_create_call_log_event = mocker.patch(
                "api.services.CallLogEventService.create_call_log_event",
                return_value=True,
            )
            mocked_create_registration = mocker.patch(
                "api.services.RegistrationService.create_registration",
                return_value=True,
            )

            handle_event_service.HandleEventService.handle_event_service(self, request)

            assert mocked_create_call_log_event.called
            assert mocked_create_registration.called
