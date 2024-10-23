# function with 2 parameters; a and b

#keyword argument
def summation(a,b):
    return a+b
print(summation(20,40))  # passing argument
print(summation(200,400))

# default argument
def subtraction(a=100,b=20):
    return a-b
print(subtraction())  # 80
print(subtraction(30,10))  # 20

# Arbitary argument
def print_animals(*animals):
    for animal in animals:
        print(animal)
print_animals("Lion", "Tiger", "Cat", "Walf")