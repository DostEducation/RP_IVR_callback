from urllib.request import Request


def mocked_request(self):
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
    return request
