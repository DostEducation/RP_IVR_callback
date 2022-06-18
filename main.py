# from pprint import pprint
from api import models, db, services
from flask import jsonify, request
import json


def callback(request):
    try:
        if request.method == "POST":
            json_data = request.get_json()
            form_data = request.form
            transaction_log_service = services.TransactionLogService()

            if json_data and json_data.get("type", None) == "retry_failed_log":
                retry_failed_webhook(transaction_log_service)
                return "Success"

            ivr_transaction_log = (
                transaction_log_service.create_new_ivr_transaction_log(form_data)
            )
            processed = process_form_data(form_data)

            if not processed:
                return jsonify(message="Something went wrong!"), 400

            transaction_log_service.mark_ivr_transaction_log_as_processed(
                ivr_transaction_log
            )
        else:
            return (
                jsonify(message="Currently, the system do not accept a GET request"),
                405,
            )
    except Exception as e:
        print(e)
        return jsonify(message="Internal server error"), 500
        
    return "Success"


def retry_failed_webhook(transaction_log_service):
    failed_ivr_logs = transaction_log_service.get_failed_ivr_transaction_log()

    for log in failed_ivr_logs:
        payload = json.loads(log.payload)
        payload["log_created_on"] = log.created_on
        log.processed = process_form_data(payload)
        log.attempts += 1
        db.session.add(log)
        db.session.commit()


def process_form_data(form_data):
    try:
        service = services.HandleEventService()
        service.handle_event_service(form_data)
        return True
    except:
        return False
