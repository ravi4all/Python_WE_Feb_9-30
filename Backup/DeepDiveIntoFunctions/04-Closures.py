# Closures

def parent():
    name = 'Ram'
    college = 'IP'

    def child():
        name = 'Shyam'
        print("Hello",name)
    def child_1():
        print("Hello",name)

    print("College", college)
    # child()
    # child_1()
    return child,child_1

c = parent()
# print(type(c))
c[1]()