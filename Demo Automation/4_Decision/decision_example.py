"""
Check given number positive or negative and even or odd
"""
number = int (input("Enter a number: "))

if number >= 0:
    if number % 2 ==0:
        print("Number is positive and even")
    else:
        print("Number is positive but odd")

else:
    if number % 2 == 0:
        print("Number is negative and even")
    else:
        print("Number is negative but odd")