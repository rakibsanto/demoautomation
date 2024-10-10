"""
if condition
    code

"""

"""
age =18
if age <= 10:
    print("Child")
else:
    print("Adult")
"""

"""
age = int(input("Enter your age: "))
if age <= 18:
    print("Child")
else:
    print("Adult")
"""

age = int(input("Enter your age: "))
if age >= 80:
    print("Old")
elif age >= 60:
    print("Senior Citizen")
elif age >= 18:
    print("Adult")
else:
    print("Child")