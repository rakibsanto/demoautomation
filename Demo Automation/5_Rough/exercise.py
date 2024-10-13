"""
txt = 'Hello World'
print(txt[2:5]) # 2-5 print
"""
"""
# Remove space from start and end
#strip()
txt = ' Hello World '
print(txt.strip())
"""

"""
# Print as upper case
message= "Hello World"
print(message.upper())

"""
"""
# Print as lower case
message= "Hello World"
print(message.lower())
"""
"""
# Replace
message= "Hello World"
new_message = message.replace("H", "J")
print(new_message)
"""

#Placeholder
age = 26
txt ="My Name is Rakib, and i am {}"
print(txt.format(age))
print(f"My Name is Rakib, and i am {age}")