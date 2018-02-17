firstname = input("Enter your first name : ")
lastname = input("Enter your last name : ")

#fullname = firstname + " " + lastname

#fullname = firstname.lower() + " " + lastname.lower()

#fullname = firstname.upper() + " " + lastname.upper()

fullname = firstname.capitalize() + " " + lastname.capitalize()

#print("Hello",fullname)
print("Hello {}".center(50).format(fullname))
