my_tuple = (1,2,3,4,5)

#Accessing Element

print(my_tuple[0]) #using postive index
print(my_tuple[-1]) #using negative index

#Slicing
print((my_tuple[0:2]))

#Length
print(len(my_tuple))

#count: returns the numer of occurrences of element
count = my_tuple.count(1)
print('Count', count)

#Iterating over the tuple

for item in my_tuple:
    print(item)