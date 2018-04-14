file = open('demo_2.txt','w')

# data = "This is some sample text"

data = ['This is some data','This is also some text']

for d in data:
    file.write(d+'\n')

file.close()