# Closures

# x = 10
def outer():
    x = 10
    print("This is outer")

    def inner():
        print("This is inner")
        print("Value of x is",x)
        return x

    def inner_2():
        print("This is inner_2")
        print("Value of x is",x+1)

    return inner,inner_2
    # inner_2()

#func = outer()
# print(x[1]())
#func[1]()

# def logic():
#     c = x()
#     print("Value returned by x function",c)

# logic()
