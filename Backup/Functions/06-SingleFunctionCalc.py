def calculator(x,y,opr):
    if opr == "+":
        return x + y
    elif opr == "-":
        return x - y
    elif opr == "/":
        return x / y
    else:
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
        "1" : "+",
        "2" : "-",
        "3" : "/",
        "4" : "*"
    }

    opr = todo.get(user_Choice)
    output = calculator(a,b,opr)
    print("Result is",output)