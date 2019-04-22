#File two.py - It will import one.py
import one

print("top-level in two.py")
one.func()

if __name__=="__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")
    
print(dir(one))     #Print the list of methods and variables in the class imported