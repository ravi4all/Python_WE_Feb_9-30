users = []
userdata = {}

def login():
    pass

def registration():
    username = input("Enter your name : ")
    flag = True
    while flag:
        usermail = input("Enter your mail ID : ")
        if len(users) >= 1:
            for user in users:
                # print(user)
                if user['EmailId'] == usermail:
                    print("ID Already Exist")
                    break
            else:
                flag = False
        else:
            break

    while True:
        userpwd = input("Enter your password : ")
        confpwd = input("Confirm Password : ")

        if userpwd != confpwd:
            print("Password do not match...")

        else:
            break

    userdata['Name'] = username
    userdata['EmailId'] = usermail
    userdata['Password'] = confpwd

    users.append(userdata.copy())

    for data in users:
        print(data)


def main():

    while True:
        print("""
        1. Login
        2. Registration
        """)

        user_ch = input("Enter your choice : ")

        todo = {
            "1" : login,
            "2" : registration
        }

        todo.get(user_ch)()

if __name__ == '__main__':
    main()