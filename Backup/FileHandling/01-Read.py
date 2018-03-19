# Open
file = open('file_1.txt','r')

# Read
# data = file.read()
# data = file.read(20)

# data = file.readline()

data = file.readlines()
print(data[2])

# Close
file.close()