def get_val(collection: dict, key, default=''):
    if key in collection.keys():
        return collection[key]
    else:
        return default
