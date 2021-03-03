# This file is treated as service layer
from api import models, db, helpers

class CallLogEventService:
    ### Main function, used to getting called from cloud function
    def handle_call_log_event(self, request):
        try:
            multi_dict = request.args
            data = {}

            data['sid'] = helpers.fetch_by_key('sid', multi_dict)
            data['cid'] = helpers.fetch_by_key('cid', multi_dict)
            data['cid_e164'] = helpers.fetch_by_key('cid_e164', multi_dict)
            data['called_number'] = helpers.fetch_by_key('called_number', multi_dict)
            data['event'] = helpers.fetch_by_key('event', multi_dict)
            data['data'] = helpers.fetch_by_key('data', multi_dict)
            data['callduration'] = helpers.fetch_by_key('callduration', multi_dict)
            data['record_duration'] = helpers.fetch_by_key('record_duration', multi_dict)
            data['total_call_duration'] = helpers.fetch_by_key('total_call_duration', multi_dict)
            data['process'] = helpers.fetch_by_key('process', multi_dict)
            data['status'] = helpers.fetch_by_key('status', multi_dict)
            data['telco_code'] = helpers.fetch_by_key('telco_code', multi_dict)
            data['outbound_sid'] = helpers.fetch_by_key('outbound_sid', multi_dict)
            data['circle'] = helpers.fetch_by_key('circle', multi_dict)
            data['operator'] = helpers.fetch_by_key('operator', multi_dict)

            self.create_call_log_event(data)
            
        except IndexError:
            print("Failed to log the call details")

    # Create a call log event
    def create_call_log_event(self, data):
        call_log_event = models.CallLogEvent(
            sid = data['sid'],
            cid = data['cid'],
            cid_e164 = data['cid_e164'],
            called_number = data['called_number'],
            event = data['event'],
            data = data['data'],
            callduration = data['callduration'],
            record_duration = data['record_duration'],
            total_call_duration = data['total_call_duration'],
            process = data['process'],
            status = data['status'],
            telco_code = data['telco_code'],
            outbound_sid  = data['outbound_sid'],
            circle = data['circle'],
            operator = data['operator'],
        )
        db.session.add(call_log_event)
        db.session.commit()