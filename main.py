# from pprint import pprint
from api import models, db, services

def callback(request):
    try:
        call_log_event_service = services.CallLogEventService()
        call_log_event_service.handle_call_log_event(request)
        print("Done updating...")
        
    except IndexError:
        print("Failed to update")
    return 'Success'
