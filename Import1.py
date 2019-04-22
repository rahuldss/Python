from math import sqrt   #to import sqrt only from math instead of all math Module
#from math import *      #to import all from math Module
import math             #to import entire math Module
import sys
import os

# print(sys.winver)
# print(sys.flags)
# print(sys.prefix)

# print(not sys)
# #sys.exit()

# print(os.name)
# print(os.environ)
# print(os.getlogin())
# print(os.getppid)

print(os.walk("D:/Narender/Projects/Python/PyCodes"))

for i in os.walk("D:/Narender/Projects/Python/PyCodes"):
    print(i)

print(math.fabs(-19))       #Float Absolute
