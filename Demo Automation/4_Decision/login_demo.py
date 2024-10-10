"""
default_username = "admin"
default_password = "123456"

# Ask the user for input

user_input_username = input("Ente Username: ")
user_input_password = input("Enter password: ")

if user_input_username == default_username and  user_input_password == default_password:
    print("Login Success")
else:
    print("Wrong Credential")

"""

user_credentials ={
    "admin" : "admin123",
    "super_user" : "super123",
    "user" : "123"
}

user_input_username = input("Ente Username: ")
user_input_password = input("Enter password: ")

if user_input_username in user_credentials:
    if user_input_password == user_credentials [user_input_username]:
        print("Login Success")
    else:
        print("Login Fail")
else:
    print("User does not exist")


