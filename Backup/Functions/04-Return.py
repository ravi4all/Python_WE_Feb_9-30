def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def div(x,y):
    return x / y

def mul(x,y):
    return x * y
# print(calc(12,22))

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

user_Choice = input("Enter your choice : ")

a = int(input("Enter first num : "))
b = int(input("Enter second num : "))

# val = add(a,b)
# print(val)

if user_Choice == "1":
    result = add(a,b)
    print("Result is",result)
elif user_Choice == "2":
    result = sub(a,b)
    print("Result is",result)
elif user_Choice == "3":
    result = div(a,b)
    print("Result is",result)
elif user_Choice == "4" or user_Choice.capitalize() == 'Mul':
    result = mul(a,b)
    print("Result is",result)
else:
    print("Wrong Choice")