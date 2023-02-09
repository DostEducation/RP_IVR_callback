# This file is treated as service layer
from api import models, app, helpers
import json
from utils.loggingutils import logger


class TransactionLogService(object):
    def create_new_ivr_transaction_log(self, jsonData):
        try:
            new_transaction_log = models.IvrCallbackTransactionLog(
                payload=json.dumps(jsonData), processed=False
            )
            helpers.save(new_transaction_log)
            logger.info(
                f"New IVR transaction log created with id: {new_transaction_log.id}"
            )
            return new_transaction_log
        except Exception as e:
            logger.error(f"Error creating new IVR transaction log: {e}")

    def mark_ivr_transaction_log_as_processed(self, ivr_transaction_log):
        try:
            ivr_transaction_log.processed = True
            helpers.save(ivr_transaction_log)
            logger.info(
                f"IVR transaction log with id {ivr_transaction_log.id} marked as processed"
            )
        except Exception as e:
            logger.error(f"Error marking IVR transaction log as processed: {e}")

    def get_failed_ivr_transaction_log(self):
        try:
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
            logger.info(
                f"Fetched {len(failed_ivr_transaction_logs)} failed IVR transaction logs"
            )
            return failed_ivr_transaction_logs
        except Exception as e:
            logger.error(f"Error fetching failed IVR transaction logs: {e}")
