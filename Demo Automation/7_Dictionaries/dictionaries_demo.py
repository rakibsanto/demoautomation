user_details = {
    "username" : "admin",
    "password" : "1234",
    "email" : "admin@gmail.com"

}

#Adding entires

user_details ["address"] = "Dhaka"
print(user_details)

#updating entires
user_details ["address"] = "BD"
print(user_details)

#Accessing Value
username_value = user_details["username"] #provide key
print(f"username: {username_value}")

#Checking if key exists in the dictionary
if 'email2' in user_details:
    print(f"Email:", user_details["email"])
else:
    print("Key not found")

#Iterating over keys
for key in user_details.keys():
    print(f"key:", key)

#Iterating over values
for value in user_details.values():
    print(f"value:", value)

#Iterating over key-value pairs
for key, value in user_details.items():
    print(key,":", value)

print(len(user_details))

#Remove entires
del user_details["address"]
print(user_details)
print(len(user_details))