"""# problem 1's solution

#get use input for upper limit
user_define_limit = int(input("Enter a integer number: "))

#initialized a veriable to store the sum

sum_of_even = 0

#loop through number from 1 to user define limit

for number in range (1, user_define_limit+1):
    if number % 2 ==0:
        sum_of_even += number

print(sum_of_even)
print(f"The sum of evens from 1 to {user_define_limit} is: {sum_of_even}")

# problem 2's solution

#get use input for upper limit
user_define_limit = int(input("Enter a integer number: "))

#initialized a veriable to store the sum

sum_of_even = 0

#loop through number from 1 to user define limit

for number in range (1, user_define_limit+1):
    if number % 2 !=0:
        sum_of_even += number

print(sum_of_even)
print(f"The sum of odd from 1 to {user_define_limit} is: {sum_of_even}")"""

#problem 3's solution

input_strint = input("Enter your word: ")
#remove space and convert to lowercase
s = input_strint.replace(" ", "").lower()

if s == s[:: -1]:
    print(f"{input_strint} is palindrome")

else:
    print(f"{input_strint} is not palindrome")

# problem 4's solution

test = input("Enter any text here: ")
r = test[::-1]
print(f"Reverse result is: " , r)