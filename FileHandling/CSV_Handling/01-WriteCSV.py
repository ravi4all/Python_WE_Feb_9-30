import csv

data = [
    'firstname,lastname'.split(','),
    'sachin,tendulkar'.split(','),
    'virat,kohli'.split(','),
    'yuvraj,singh'.split(','),
    'ms,dhoni'.split(',')
]
with open('data.csv','w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)