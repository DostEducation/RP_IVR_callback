# from pprint import pprint
from api import models, db, services
from flask import jsonify, request


def callback(request):
    try:
        if request.method == "POST":
            formData = request.form
            transaction_log_service = services.TransactionLogService()
            ivr_transaction_log = (
                transaction_log_service.create_new_ivr_transaction_log(formData)
            )
            service = services.HandleEventService()
            service.handle_event_service(request)
            transaction_log_service.mark_ivr_transaction_log_as_processed(
                ivr_transaction_log
            )
        else:
            return (
                jsonify(message="Currently, the system do not accept a GET request"),
                405,
            )
    except IndexError:
        return jsonify(message="Something went wrong!"), 400
    return "Success"
