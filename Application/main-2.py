from datetime import datetime

users = []
userdata = {}

posts = []
postdata = {}

# data = [
#     {'username' : 'Ram', 'email':'....'},
#     {'username' : 'Ram', 'email':'....'}
# ]

def post_something(useremail):
    post = input("Enter your post : ")
    current_date = datetime.now().date()

    postdata['post'] = post
    postdata['useremail'] = useremail
    postdata['date'] = current_date.isoformat()

    posts.append(postdata.copy())

    for data in posts:
        print(data)

    # login_success()

def view_profile(useremail):
    current_user = list(filter(lambda x : x['EmailId'] == useremail, users))
    username = current_user[0]['Name']
    print("Hello",username)
    userpost = list(filter(lambda x: x['useremail'] == useremail, posts))

    for data in userpost:
        print("Post",data['post'])
        print("Username",username)
        print("Date",data['date'])

def update_profile():
    pass

def delete_profile():
    pass

def errHandler_2(*args):
    print("Wrong Choice")

def login_success(useremail, username):
    while True:
        print("""
        1. Post Something
        2. View Profile
        3. Update Profile
        4. Delete Profile
        5. Logout
        """)

        todo = {
            "1" : post_something,
            "2" : view_profile,
            "3" : update_profile,
            "4" : delete_profile
        }

        userinput = input("Enter your choice : ")

        if userinput == "5":
            break

        todo.get(userinput, errHandler_2)(useremail)

def login():
    useremail = input("Enter your emailID : ")
    userpwd = input("Enter your password : ")

    for data in users:
        if data['EmailId'] == useremail and data['Password'] == userpwd:
            print("Login Success")
            login_success(data['EmailId'], data['Name'])
            break
    else:
        print("Login Failed")

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

def errHandler():
    print("Wrong Choice")

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

        todo.get(user_ch, errHandler)()

if __name__ == '__main__':
    main()