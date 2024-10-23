#global scope
c =2
def summation():
    a=10 #local scope
    b=20
    #print(a+b+c)
    return(a+b+c)
    print("Hello World")  # unreachable statement

print(summation())  # print single time

def subtraction():
    a=10
    b=5
    #print(a-b-c)
    #return(a-b-c)
    return summation() -a -b
print(subtraction())

result = summation() + subtraction()
print(result)

def get_name_and_age():
    name= "Smith"
    age = "26"
    return name, age
print(get_name_and_age())  # ('Smith', '26')
print(get_name_and_age()[0])  # Smith

name_age = get_name_and_age()  # Smith
print(name_age[0])