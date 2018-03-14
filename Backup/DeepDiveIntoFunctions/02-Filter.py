def even(num):
    return num % 2 == 0

# even_num = []
# def even(num):
#     if num % 2 == 0:
#         even_num.append(num)
#
#     return even_num

numbers = [12,13,14,15,16,17,18,19,20]

# for num in numbers:
#     print(even(num))

# e_num = []
# for num in numbers:
#     e_num = even(num)
#
# print(e_num)

e_num = list(filter(even, numbers))
print(e_num)