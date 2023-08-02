import csv

def load_csv(file_name):
    with open(file_name,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data=list()
        for row in reader:
            data.append(row)
        return data
