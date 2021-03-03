def fetch_by_key(key, data):
    if key in data:
        return data[key]
    return None