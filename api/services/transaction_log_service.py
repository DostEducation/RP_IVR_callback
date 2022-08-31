# This file is treated as service layer
from api import models, app, helpers
import json


class TransactionLogService(object):
    def create_new_ivr_transaction_log(self, jsonData):
        new_transaction_log = models.IvrCallbackTransactionLog(
            payload=json.dumps(jsonData), processed=False
        )
        helpers.save(new_transaction_log)
        return new_transaction_log

    def mark_ivr_transaction_log_as_processed(self, ivr_transaction_log):
        ivr_transaction_log.processed = True
        helpers.save(ivr_transaction_log)

    def get_failed_ivr_transaction_log(self):
        failed_ivr_transaction_logs = (
            models.IvrCallbackTransactionLog.query.filter(
                models.IvrCallbackTransactionLog.processed == False
            )
            .filter(
                models.IvrCallbackTransactionLog.attempts
                < app.config["MAX_RETRY_ATTEMPTS_FOR_LOGS"]
            )
            .order_by(models.IvrCallbackTransactionLog.id)
            .limit(app.config["RETRY_LOGS_BATCH_LIMIT"])
            .all()
        )

        return failed_ivr_transaction_logs
