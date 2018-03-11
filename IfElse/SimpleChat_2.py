print("Welcome".center(100))
print("How may I assist you ???")

hello_intent = ['hi','hello','hey','hie','yo']
bye_intent = ['bye','bie','take care','see you']

while True:
    user = input("Enter your message : ")

    userMessage = user.lower()

    if userMessage in hello_intent:
        print("Hello There")
    elif userMessage in bye_intent:
        print("Bye, Take Care !!!")
    else:
        print("I dont't understand")
        break