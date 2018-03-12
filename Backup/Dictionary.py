# Unordered Type of Data
# Dict - Key : Value pair
# JSON/Javascript Object/Hash Map

my_dict = {'id':101,'name':'Ram','age':29}
# print(type(my_dict))
# print(my_dict)

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

print(my_dict['name'])

my_dict['company'] = 'TCS'
print(my_dict)

user_choice = input("Enter your choice : ")

print(my_dict.get(user_choice))