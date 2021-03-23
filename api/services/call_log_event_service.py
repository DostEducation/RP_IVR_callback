# This file is treated as service layer
from api import models, db

class CallLogEventService:
    ### Main function, used to getting called from cloud function
    def handle_call_log_event(self, request):
        try:
            data = {}
            data['call_sid'] = request.args.get('CallSid')
            data['account_sid'] = request.args.get('AccountSid')
            data['from_number'] = request.args.get('From')
            data['to_number'] = request.args.get('To')
            data['call_status'] = request.args.get('CallStatus')
            data['direction'] = request.args.get('Direction')
            data['parent_call_sid'] = request.args.get('ParentCallSid')
            data['telco_code'] = request.args.get('TelcoCode')
            data['telco_status'] = request.args.get('TelcoStatus')
            data['dial_time'] = request.args.get('DialTime')
            data['pick_time'] = request.args.get('PickTime')
            data['end_time'] = request.args.get('EndTime')
            data['duration'] = request.args.get('Duration')
            self.create_call_log_event(data)
            
        except IndexError:
            print("Failed to log the call details")

    # Create a call log event
    def create_call_log_event(self, data):
        call_log_event = models.CallLogEvent(
            call_sid = data['call_sid'],
            account_sid = data['account_sid'],
            from_number = data['from_number'],
            to_number = data['to_number'],
            call_status = data['call_status'],
            direction = data['direction'],
            parent_call_sid = data['parent_call_sid'], 
            telco_code = data['telco_code'],
            telco_status = data['telco_status'],
            dial_time = data['dial_time'],
            pick_time = data['pick_time'],
            end_time = data['end_time'],
            duration = data['duration'],
        )
        db.session.add(call_log_event)
        db.session.commit()