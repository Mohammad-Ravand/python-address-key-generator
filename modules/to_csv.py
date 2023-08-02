import csv

def json_to_csv(data, csv_file):
    # Load the JSON data
    # data = json.loads(json_data)

    # Extract the header fields from the first row
    header = list(data[0].keys())
    
    # Open the CSV file for writing with UTF-8 encoding
    with open(csv_file, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)

        # Write the CSV header
        writer.writeheader()

        # Write the CSV rows
        for row in data:
            # Convert values to UTF-8 encoding
            encoded_row = {key: str(value).encode('utf-8').decode('utf-8') for key, value in row.items()}
            writer.writerow(encoded_row)

# data = read_data_from_json('./original_old.json')
# json_to_csv((data),'./store_old.csv')