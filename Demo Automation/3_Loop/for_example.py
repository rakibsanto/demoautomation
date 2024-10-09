#looping through a list
"""
#single print all item
fruits = ['Apple', 'Orange', 'Banana', 'Mango']
for fruit in fruits:
    print(fruit)
"""
"""
#print apple 3 times then other item 1 time
fruits = ['Apple', 'Orange', 'Banana', 'Mango']
for index, fruit in enumerate(fruits):
    if index == 0:
        for _ in range(2):
            print(fruits[0])
    print(fruit)
 
"""

"""
#all items should be 3 times
fruits = ['Apple', 'Orange', 'Banana', 'Mango']
for fruit in enumerate(fruits):
        for _ in range(3):
          print(fruit)
"""
"""
message = "Hello World"
for letter in message:
    print(letter)
print(len(message))
"""
"""
#Nested loop 2D grid
for i in range(3):
    for j in range(3):
        print(i,j)
"""
#Nested loop 3D grid

for i in range(3):
    for j in range(3):
        for k in range(3):
             print(i,j,k)
