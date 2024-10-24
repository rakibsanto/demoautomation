from module_demo1 import summation,subtraction   # same package
from module_demo2 import multiply,division
print(summation(10,20))
print(subtraction(50,10))
print(multiply(5,2))
print(division(10,2))


"""
from packagename.filename import functionname # from externam package
from module_demo1 import *   # import all 
import modulename   # always need to call the modulename
import modulename as md  # module rename
"""

# function rename
from module_demo1 import summation as sm  #sumation is rename as sm
print(sm(1,2))

import module_demo2 as md2
print(md2.division(10,5))