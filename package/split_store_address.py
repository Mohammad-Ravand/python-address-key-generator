def split_store_address(keys, address_string):
    try:
        
        address_string = address_string.strip()
        split_array = address_string.split()
        second = [''] * len(split_array)

        split_array = list(filter(None, split_array))
        
        

        key_names = [key['name'] for key in keys]
        for address_index, address_value in enumerate(split_array):
            remove_space_address_value = address_value.replace(' ', '')
            find = key_names.index(remove_space_address_value) if remove_space_address_value in key_names else -1
            if find == -1:
                # Not found in keys
                continue
            else:
                second[address_index] = {}
                key = keys[find]
                second[address_index]['key_id'] = key['id']
                second[address_index]['type'] = key['type']
                second[address_index]['index'] = address_index

        #secion two
        result = []

        # Specify type of operation based on the type of mainkey
        # 'normal','before','before:int','after','after:int'

        second = [item for item in second if item]

        before = 0
        for second_index, key in enumerate(second):
            if key['type'] == 'before:int':
                if before != second_index:
                    item_address = [item for item in reversed(split_array[before:second_index]) if isinstance(item, int)]

                    key['address'] = ' '.join(item_address)
                    if len(key['address']) > 0:
                        result.append(key)
            elif key['type'] == 'before':
                if before != second_index:
                    item_address = split_array[before:second_index+1]
                    key['address'] = ' '.join(item_address)
                    if len(key['address']) > 0:
                        result.append(key)
            else:
                pass
            before = second_index

        #section three
        h = {}
        second_iter = iter(second)
        second_iter1 = (iter(second))
        next_key = next(second_iter1,None)

        
        while True:
                current = next(second_iter,None)
                
                next_key = next(second_iter1,None)
               
                
                if current is None:
                    break
                if next_key is None:
                    next_key = current
                    item_address = split_array[current['index']:]
                    current['address'] = ' '.join(item_address)
                    if len(current['address']) > 0:
                        result.append(current)

                if current['type'] == 'normal':
                    if current['index'] != next_key['index']:
                        item_address = split_array[current['index']:next_key['index']]
                        current['address'] = ' '.join(item_address)
                        if len(current['address']) > 0:
                            result.append(current)
                elif current['type'] == 'after':
                    if current['index'] != next_key['index']:
                        item_address = split_array[current['index'] + 1:next_key['index'] - 1]
                        current['address'] = ' '.join(item_address)
                        if len(current['address']) > 0:
                            result.append(current)
                elif current['type'] == 'after:int':
                    if current['index'] != next_key['index']:
                        item_address = split_array[current['index']:next_key['index']]
                        current['address'] = ' '.join(item_address)
                        if len(current['address']) > 0:
                            result.append(current)
                else:
                    if current['index'] != next_key['index']:
                        item_address = split_array[current['index'] + 1:next_key['index'] - 1]
                        current['address'] = ' '.join(item_address)
                        if len(current['address']) > 0:
                            result.append(current)

            

        return result
    except Exception as e:
        print(str(e))
        raise
# keys = [
#     {'id': 1, 'name': 'Street', 'type': 'normal'},
#     {'id': 2, 'name': 'city', 'type': 'normal'},
#     {'id': 3, 'name': 'zip', 'type': 'normal'}
# ]
# address_string = " 1234 city LA Elm Street Chicago zip 60601 "
# result = new_splitAddress(keys, address_string)
# print(result)