"""
# SyntaxError means syntax missing
print("Error
"""
""" 
#IndentationError means format missing
if True:
print("IndentationError")
"""

"""
#NameError
name="Smith"
print(Name)
"""

"""
#TypeError
result = 10+'5'
print(result)
"""

"""
#ZeroDivisionError
result = 20/0
print(result)
"""

"""
#indexError
my_list = [1,2,3,4]
print(my_list[5])
"""

"""
#ValueError
user_input = input("Enter a number: ")
number = int(user_input)
print(number)
"""

"""
#KeyError
user = {
    'name': 'smith',
    'age': '15',
    'pass': 'password'
}
print(user['email'])
"""