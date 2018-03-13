def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def div(x,y):
    return x / y

def mul(x,y):
    return x * y

while True:
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    user_Choice = input("Enter your choice : ")

    a = int(input("Enter first num : "))
    b = int(input("Enter second num : "))

    todo = {
        "1" : add,
        "2" : sub,
        "3" : div,
        "4" : mul
    }

    output = todo.get(user_Choice)(a,b)   # add
    print("Result is",output)