# from pprint import pprint
from api import models, db, services
from flask import jsonify, request


def callback(request):
    try:
        if request.method == "POST":
            call_log_event_service = services.CallLogEventService()
            call_log_event_service.handle_call_log_event(request)
        else:
            return (
                jsonify(message="Currently, the system do not accept a GET request"),
                405,
            )
    except IndexError:
        return jsonify(message="Something went wrong!"), 400
    return "Success"
