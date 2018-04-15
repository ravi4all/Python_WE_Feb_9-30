try:
    file = open('data.txt','w')
    file.read()

except FileNotFoundError:
    print("File donot exist")

finally:
    print("This will always execute")
    file.close()

# file = open('data.txt','r')
# file.read()
# print("This is outside try and except")