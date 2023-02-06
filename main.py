# from pprint import pprint
from api import models, db, services
from flask import jsonify, request
import json
import logging

logger = logging.getLogger(name)
logger.setLevel(logging.DEBUG)


def callback(request):
    if request.method == "POST":
        json_data = request.get_json()
        form_data = request.form
        transaction_log_service = services.TransactionLogService()

        try:
            if json_data and json_data.get("type", None) == "retry_failed_log":
                retry_failed_webhook(transaction_log_service)
                return "Success"

            ivr_transaction_log = (
                transaction_log_service.create_new_ivr_transaction_log(form_data)
            )
        except Exception as e:
            logger.error("Issues with Transaction logs creation")
            logger.error(e)

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
    logger.info("Retrying failed IVR logs: Done")


def process_form_data(form_data):
    try:
        service = services.HandleEventService()
        service.handle_event_service(form_data)
        return True
    except Exception as e:
        logger.error("Exception occurred while handling Event Service")
        logger.error(e)
        return False
