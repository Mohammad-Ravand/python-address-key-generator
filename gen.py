from modules.csv_file import load_csv
from modules.to_csv import json_to_csv
from modules.json_file import read_data_from_json,insert_and_read_json
from package.replace_subkeys import replace
from package.split_store_address import split_store_address
from package.format_keys import format_keys
from package.numbers import replaceAllNumbers
import re
import math

# load all data input
# keys = read_data_from_json('./subkey_genrate/generate.json')


def main():
    stores = load_csv('./subkey_genrate/tehran.csv')

    keys = set()
    values = set()  

    # start operation

    try:
        for store in stores:
            
            
            
            if(len(values)):
                insert_and_read_json(list(values),'./subkey_genrate/values.json')
            
            if(store['completed']==True):
                show_progress(store_index,len(stores))
                values = values.union(setValues(split_address,keys))
                continue
            
            keys = set(read_data_from_json('./subkey_genrate/keys.json'))
            values = set(read_data_from_json('./subkey_genrate/values.json'))
            
            store_index = stores.index(store)
            
            address = str(store['address'])
            
            # repalce all number to empty
            address =  re.sub( r'\d+', '', address)
            
            split_address= address.strip().split(' ')
            
            
            
            
            for item in split_address :
                if(item.strip() in keys):
                    split_address.remove(item.strip())
                    
                    
            show=False 
            for item in split_address:
                item_index = split_address.index(item)
                if(item.strip() not in keys and item.strip() not in values):
                    show=True
                
            if(show==False):
                show_progress(store_index,len(stores))
                setValues(split_address,keys)
                continue
            
            print(address)
            print('---------------------------------')
            print('')
            for item in split_address:
                item_index = split_address.index(item)
                if(item.strip() not in keys and item.strip() not in values):
                    print(f'=> {item_index} ==> {item}')
                
          

            input_answer=''
            while(True):
                input_answer = input('insert your number for key:=> ')
                if(input_answer=='n' or len(input_answer)>0 ):
                    break
                else:
                    continue
            if(input_answer=='n'):
                show_progress(store_index,len(stores))
                values = values.union(setValues(split_address,keys))
                continue
            if(input_answer=='cp'):
                store['completed']= True
                stores[store_index] = store
                show_progress(store_index,len(stores))
            
                # save stores
                values = values.union(setValues(split_address,keys))
                json_to_csv(stores,'./subkey_genrate/tehran.csv')
                insert_and_read_json(list(keys),'./subkey_genrate/keys.json')
                continue
            
            input_answer_split = input_answer.split('.')
            for answer_index in input_answer_split:
                key_name = ''
                if('+' in answer_index):
                    plus_split = answer_index.split('+')
                    
                    for item in plus_split:
                        if(len(key_name)==0):
                            key_name= split_address[int(item)]
                        else:
                            key_name+=" "+ split_address[int(item)]
                    keys.add(key_name)
                elif('-' in answer_index):  
                    dash_split = answer_index.split('-')
                    
                    
                    for item in dash_split:
                        if(len(key_name)==0):
                            key_name= split_address[int(item)]
                        else:
                            key_name+=""+ split_address[int(item)]
                    keys.add(key_name)
                else:
                    key_name = split_address[int(answer_index)]
                    if(key_name not in keys):
                        keys.add(key_name)
            # add all items except one that exist in keys
            
            store['completed']= True
            stores[store_index] = store
            show_progress(store_index,len(stores))
            values = values.union(setValues(split_address,keys))
            
            # save stores
            json_to_csv(stores,'./subkey_genrate/tehran.csv')
            show_progress(store_index,len(stores))
            insert_and_read_json(list(keys),'./subkey_genrate/keys.json')
            
            
    except Exception as e:
        print(str(e))
        raise
    # end operation


def show_progress(index,total):
    print('')
    print(f'***********{index} / {total} % ***************')
    print('')
    
    
def setValues(split_address,keys):
    v = set()
    for item in split_address:
        if(item not in keys):
            v.add(item)
    return v

main()