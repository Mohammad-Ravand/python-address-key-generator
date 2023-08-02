def replace(address:str,keys:list):
    for key in keys:
        key_name = key['name']
        sub_keys = key['subkeys']
        sub_key_names  = [subkey['name'] for subkey in sub_keys ]
        
        for sub_key_name in sub_key_names:
            if(sub_key_name in address):
                address = address.replace(sub_key_name,key_name)
    return address