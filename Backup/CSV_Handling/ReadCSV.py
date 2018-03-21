import csv

path = 'data.csv'

users = []
with open(path, 'r') as file:
    reader = csv.reader(file)

    for data in reader:
        # print(data)
        users.append(data)

    print(users)