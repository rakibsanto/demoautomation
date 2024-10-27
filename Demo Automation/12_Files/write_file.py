try:
    file_obj = open('testfile.txt' , 'w')
    fileText = file_obj.write('File text write')
    file_obj.close()
except Exception as e:
    print(f"ExceptionType: {type(e)} Exception details: {e}")