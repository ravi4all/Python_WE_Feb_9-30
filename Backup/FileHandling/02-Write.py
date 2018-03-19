file = open('file_2.txt','w')

# data = "This file is written using python script"

data = ["Ram","Shyam","Ajay","Gopal"]

# file.write(data)

for d in data:
    file.write(d+"\n")

file.close()