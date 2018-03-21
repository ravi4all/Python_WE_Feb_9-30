import csv

data = [
    'FirstName, LastName'.split(","),
    'Sachin,Tendulkar'.split(","),
    'MS,Dhoni'.split(","),
    'Virat,Kohli'.split(","),
    'Yuvraj,Singh'.split(",")
]

# file = open('data.csv','w')
# file.close()

with open('data.csv','w', newline='') as file:
    writer = csv.writer(file)

    for d in data:
        writer.writerow(d)