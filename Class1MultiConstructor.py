class MultiConstructorClass():
    def __init__(self):
        print("Constructor __init__")

    @classmethod
    def myConstructor1(cls,a,b):
        print("called myConstructor1 : ",a,b)

    @classmethod
    def myConstructor2(cls,a,b,c):
        print("called myConstructor2 : ",a,b,c)

obj=MultiConstructorClass()     #With Default constructor
obj.myConstructor1(1,2)
obj.myConstructor2(1,2,3)

obj1=MultiConstructorClass.myConstructor1(1,2)      #With Custom constructor
