# BaseException
# TypeError
# ZeroDivisionError
def calc():
    try:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        print(a+b)
        print(a-b)
        print(a/b)
        print(a*b)
    # except BaseException as ex:
    #     print(ex)
        # print("Some Error")
        # calc()
    except ZeroDivisionError:
        print("Cannot divide by zero")
        calc()
    except ValueError:
        print("You pressed something wrong")
        calc()


calc()