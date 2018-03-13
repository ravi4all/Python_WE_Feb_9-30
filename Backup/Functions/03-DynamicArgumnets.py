# Dynamic Arguments
# * - args
# ** - kwargs

def emp(id,name,salary,*address):
    print("ID : {}".format(id))
    print("Name : {}".format(name))
    print("Salary : {}".format(salary))
    # print("Address : {}".format(address))
    # for addr in address:
    #     print("Address :",addr)

    # for i in range(len(address)):
    #     print("Address {} : {}".format(i,address[i]))

    for i,addr in enumerate(address):
        print("Address {} : {}".format(i+1,addr))

# emp(101,'Ram',15000,['Rohini','Dilshad Garden', 'Ghaziabad'])
# emp(101,'Ram',15000,'Rohini','Dilshad Garden', 'Ghaziabad')


def student(**details):
    print(details)
    # print(details.items())
    # for s in details.items():
    #     print(s)

student(name='Ram',age=18,college='IP')
student(name='Shyam',college='DU')
student(name='John',age=19,city='Delhi',college='DU')