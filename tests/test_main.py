from flask import jsonify, Flask
import main
import json
from tests import mocked_request


class TestMain:
    def test_main_if_request_is_post(self, mocker):
        app = Flask("__FLASK__")
        with app.app_context():
            request = mocked_request.mocked_request(self)
            mocked_handle_event_service = mocker.patch(
                "api.services.HandleEventService.handle_event_service",
                return_value=True,
            )

            response = main.callback(request)
            assert mocked_handle_event_service.called
            assert response == "Success"

    def test_main_if_request_is_get(self, mocker):
        app = Flask("__FLASK__")
        with app.app_context():
            request = mocked_request.mocked_request(self)
            request.method = "GET"
            mocked_handle_event_service = mocker.patch(
                "api.services.HandleEventService.handle_event_service",
                return_value=True,
            )
            response = main.callback(request)

            assert (
                json.loads(response[0].get_data())["message"]
                == "Currently, the system do not accept a GET request"
            )
            assert response[1] == 405
