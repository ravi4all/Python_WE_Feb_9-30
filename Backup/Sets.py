# Sets
a = {2,3,4,5,6}
b = {6,5,7,8,1}

data = ['Ram','Shyam','Amit','Ravi','Ram','Ravi','Ajay','Amit']
data = set(data)
print(data)

# print(a & b)
# print(a | b)
# print(a - b)

print(a.intersection(b))
print(a.union(b))
print(a.difference(b))