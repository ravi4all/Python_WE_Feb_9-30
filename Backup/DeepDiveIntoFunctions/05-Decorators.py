def profile(login):
    print("This is profile")
    login()

@profile
def login_req():
    print("Login First")

# profile(login_req)