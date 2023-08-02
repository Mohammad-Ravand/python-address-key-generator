import json


def read_data_from_json( filename):
    # Read JSON data from file
    with open(filename, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    return json_data


def insert_and_read_json(data, filename):
    # Insert JSON data to file
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

    