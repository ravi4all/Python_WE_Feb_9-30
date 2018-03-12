a = [10,20,30,40,50,60]
b = (10,20,30,40,50,60)

print(type(a), type(b))

print(a[1], b[2])

print(a[0:3], b[0:3])

# print("Before :",a)
# a[0] = 'Bye'
# print("After :",a)

print("Before :",b)
b[0] = 'Bye'           # Tuples are immutable (Cannot be modified)
print("After :",b)