# User defined Exception
# raise
# assert

def atm():
    user_pin = input("Enter your PIN : ")
    total_bal = 10000
    try:
        if user_pin == "1234":
            print("Login Success")
        else:
            print("Login Failed")
            raise ValueError("Wrong PIN")

    except ValueError as err:
        print(err)
        atm()

    else:
        amount = int(input("Enter amount you want to withdraw : "))
        if amount > total_bal:
            print("Invalid amount")
        else:
            total_bal -= amount
        print("Remaining balance is", total_bal)

atm()