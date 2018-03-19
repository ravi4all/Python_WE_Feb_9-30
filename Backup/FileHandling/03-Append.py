file = open('file_2.txt','a')

# data = "This file is written using python script"

data = ["John","Shawn","Tom","Jim","Robert"]

# file.write(data)

for d in data:
    file.write(d+"\n")

file.close()