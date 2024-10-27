#try

"""
try:
    result = 10 + '5'
    print(result)
except Exception as e:
    # print("Exception occurred: ", e)
    print(f"ExceptionType:{type(e)} Exception details: {e}")

print("Hello World")
"""

"""
try:
    my_list = [1, 2, 3, 4]
    print(my_list[5])
except Exception as e:
    print(f"ExceptionType:{type(e)}  Exception details: {e}")
"""

#FileNotFoundError

try:
    file_obj = open('testfile2.txt' , 'r')
    fileText = file_obj.read()
    print(fileText)
    file_obj.close()
except Exception as e:
    print(f"ExceptionType: {type(e)} Exception details: {e}")