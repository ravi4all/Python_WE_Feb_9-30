# By default mode is read...
file = open('demo_1.txt')

# file = open('Football.png','rb')

# data = file.read()
# data = file.read(15)

# data = file.readline()

data = file.readlines()
print(data)

file.close()

# file_1 = open('ball_2.png','wb')
#
# file_1.write(data)
#
# file_1.close()