def atm():
    user_pin = input("Enter your PIN : ")
    total_bal = 10000
    if user_pin == "1234":
        print("Login Success")
    else:
        print("Login Failed")

    amount = int(input("Enter amount you want to withdraw : "))
    if amount > total_bal:
        print("Invalid amount")
    else:
        total_bal -= amount

    print("Remaining balance is", total_bal)

atm()