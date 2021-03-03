# from pprint import pprint
from api import models, db, services

def callback_backup(request):

    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # print(request.method)
    # pprint(globals())
    # pprint(locals())

    # print('Request DICT ->')
    # print(request.__dict__)
    
    # print('Request HEADERS ->')
    # print(request.headers)
    
    # print('Request ARGS ->')
    # print(request.args)
    # if request.args.get('circle')
    #     print("value for circle is:" + request.args.get('circle1') + "-done printing")
    print(request.values)

    print("all post data")
    # print("--->" + request.data)
    multi_dict = request.args
    if "circle" in multi_dict:
        circle=multi_dict.get('circle')
        print('circle=' + circle)

    sid=multi_dict.get('sid')
    # circle=multi_dict.get('circle')
    # system_phone=multi_dict.get('cid_e164')
    # event=multi_dict.get('event')
    # cid_type=multi_dict.get('cid_type')
    # cid=multi_dict.get('cid')
    # called_number=multi_dict.get('called_number')
    # request_time=multi_dict.get('request_time')

    print('sid=' + sid)
    # print('circle=' + circle)
    # print('system_phone=' + cid_e164)
    # print('event=' + event)
    # print('cid_type' + cid_type)
    # print('cid=' + cid)
    # print('called_number=' + called_number)
    # print('request_time=' + request_time)



    for key in multi_dict:
        print(multi_dict.get(key))
        # print (multi_dict.getlist(key))
    
    print("all post form data")

    mdict = request.form

    for key in mdict:
        print ('form key->'+ key + '<-value->' +mdict[key])
    
    # request_json = request.get_json()
    # if request.args and 'message' in request.args:
    #     print('first line')
    #     print(request.args)
    #     return request.args.get('message')
    # elif request_json and 'message' in request_json:
    #     print('second line')
    #     return request_json['message']
    # else:
    #     print('final line')
    #     return f'Hello World!'

    return "success"

def callback(request):
    try:
        call_log_event_service = services.CallLogEventService()
        call_log_event_service.handle_call_log_event(request)
        print("Done updating...")
        
    except IndexError:
        print("Failed to update")
    return 'Success'
