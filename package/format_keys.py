def format_keys(keys:list):
    formated_keys = list()
    
    for key in keys:
        simple_key_format= {'id': 1, 'name': '', 'type': 'normal'}

        key_index = keys.index(key)
        simple_key_format['name'] = key['name']
        simple_key_format['id'] = (keys.index(key))+1
        formated_keys.append(simple_key_format)
    return formated_keys
        