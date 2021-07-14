# This file is treated as service layer
from api import models, helpers
import json


class TransactionLogService(object):
    def create_new_ivr_transaction_log(self, jsonData):
        new_webhook_log = models.IvrCallbackTransactionLog(
            payload=json.dumps(jsonData), processed=False
        )
        helpers.save(new_webhook_log)
        return new_webhook_log

    def mark_ivr_transaction_log_as_processed(self, webhook):
        webhook.processed = True
        helpers.save(webhook)
