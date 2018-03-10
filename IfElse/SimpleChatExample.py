print("Welcome".center(100))
print("How may I assist you ???")

while True:
    user = input("Enter your message : ")

    userMessage = user.lower()

    if userMessage == "hi":
        print("Hi")
    elif userMessage == "hello":
        print("Hi")
    elif userMessage == "how are you":
        print("I am fine")
    elif userMessage == "bye":
        print("Bye")
    else:
        print("I dont't understand")
        break