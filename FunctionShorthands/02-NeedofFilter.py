# def even_num(num):
#     return num % 2 != 0

# List comprehension
numbers = [i for i in range(1,101)]

# e = list(filter(even_num, numbers))
e = list(filter(lambda num : num % 2 == 0, numbers))
print(e)