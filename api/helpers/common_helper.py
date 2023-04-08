from datetime import datetime, timedelta


def current_ist_time():
    return datetime.utcnow() + timedelta(minutes=330)
