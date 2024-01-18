import csv

with open('teksts.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 2:
            print(row[1])