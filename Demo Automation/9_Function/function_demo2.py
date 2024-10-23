#global scope
c =2
def summation():
    a=10 #local scope
    b=20
    print(a+b+c)

summation()  # print single time
for i in range(5):  #print 5 time
    summation()

def subtraction():
    a=10
    b=5
    print(a-b-c)
subtraction()