class Class1():
    '''
    My First Class named Class1
    '''
    def __init__(self):         #Constructor
        self.__pri=("I am private.")
        self._pro=("I am protected.")
        self.pub=("I am public.")

    def func1(self):
        print("func1 of Class1")

    def funcHelp(self):
        print(self.__dict__)
        print(Class1.__name__)
        print(self.__doc__)
        print(self.__module__)
        print(Class1.__bases__)

    def __privateMethod(self):
        print("Private Method")

    def _protectedMethod(self):
        print("Protected Method")

    def publicMethod(self):
        print("Public Method")

    def __del__(self):          #Destructor
        print("Destructor")

obj=Class1()
obj.func1()
obj.funcHelp()
#print(obj.__pri)   #Private cannot be accessible
print(obj._Class1__pri)   #Private can be accessible by using classname also
print(obj._pro)
print(obj.pub)

#obj.__privateMethod()   ##not accessible
obj._Class1__privateMethod()   ##Private accessible by using classname also
obj._protectedMethod()
obj.publicMethod()