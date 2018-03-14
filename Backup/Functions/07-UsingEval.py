def calculator(x,y,opr):
    expression = x + opr + y
    return eval(expression)      # Evaluate

while True:
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    user_Choice = input("Enter your choice : ")

    a = input("Enter first num : ")
    b = input("Enter second num : ")

    todo = {
        "1" : "+",
        "2" : "-",
        "3" : "/",
        "4" : "*"
    }

    opr = todo.get(user_Choice)
    output = calculator(a,b,opr)
    print("Result is",output)