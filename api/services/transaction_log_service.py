# This file is treated as service layer
from api import models, db, app
import json


class TransactionLogService(object):
    def create_new_ivr_transaction_log(self, jsonData):
        new_transaction_log = models.IvrCallbackTransactionLog(
            payload=json.dumps(jsonData), processed=False
        )
        db.session.add(new_transaction_log)
        db.session.commit()
        return new_transaction_log

    def mark_ivr_transaction_log_as_processed(self, ivr_transaction_log):
        ivr_transaction_log.processed = True
        db.session.add(ivr_transaction_log)
        db.session.commit()

    def get_failed_ivr_transaction_log(self):
        failed_ivr_transaction_logs = (
            models.IvrCallbackTransactionLog.query.filter_by(processed=False)
            .limit(app.config["RETRY_LOGS_LIMIT"])
            .all()
        )

        return failed_ivr_transaction_logs
