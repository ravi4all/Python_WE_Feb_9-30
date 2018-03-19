# numbers = []
#
# for i in range(1,101):
#     if i % 2 == 0:
#         numbers.append(i)

# numbers = [i for i in range(1,101)]

numbers = [i for i in range(1,101) if i % 2 == 0]

print(numbers)