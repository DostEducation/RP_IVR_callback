# This file is treated as service layer
from api import models, db, helpers

class CallLogService:
    ### Main function, used to getting called from cloud function
    def handle_call_log(self, request):
        try:
            multi_dict = request.args
            data = {}
            
            data['call_sid'] = helpers.fetch_by_key('sid', multi_dict)
            data['circle'] = helpers.fetch_by_key('circle', multi_dict)
            data['system_phone'] = helpers.fetch_by_key('cid_e164', multi_dict)
            data['event'] = helpers.fetch_by_key('event', multi_dict)
            data['cid_type'] = helpers.fetch_by_key('cid_type', multi_dict)
            data['cid'] = helpers.fetch_by_key('cid', multi_dict)
            data['called_number'] = helpers.fetch_by_key('called_number', multi_dict)
            data['request_time'] = helpers.fetch_by_key('request_time', multi_dict)
            data['total_call_duration'] = helpers.fetch_by_key('total_call_duration', multi_dict)
            
            if data['event'] == 'NewCall':
                data['call_type'] = 'outbound'

        except IndexError:
            print("Failed to log the call details")

    # Create a call log
    def create_call_logs(self, data):
        user_phone = data['called_number']

        call_log = models.CallLog(
            call_sid = data['call_sid'],
            call_type =  'Outbound',
            user_phone_number =  data['called_number'],
            system_phone_number = data['system_phone'],
            listen_seconds = data['total_call_duration'],
            circle = data['circle'],
            # TODO: Need to map the below fields with the details coming from RapidPro
            # registration_id =  data[''],
            # user_id =  data[''],
            # flow_run_uuid = data['run_uuid'],
            # call_type =  data['call_type'],
            # scheduled_by =  data[''],
            # status = data[''],
            
        )
        db.session.add(call_log)
        db.session.commit()
