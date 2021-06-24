from flask import jsonify, Flask
import pytest
from urllib.request import Request
import main
import json


class TestMain:
    def test_main(self, mocker):
        app = Flask("__FLASK__")
        with app.app_context():
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
            mocked_handle_event_service = mocker.patch(
                "api.services.HandleEventService.handle_event_service",
                return_value=True,
            )

            response = main.callback(request)

            assert mocked_handle_event_service.called
            assert response == "Success"

            request.method = "GET"
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
