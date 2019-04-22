class ClsParent():
    def __init__(self):
        print("Parent init")

    def methodBase(self):
        print("method Base")

class ClsChild(ClsParent):
    def __init__(self):
        print("Child init")

    def methodChild(self):
        print("method Child")


obParent=ClsParent()
obParent.methodBase()

obChild=ClsChild()
obChild.methodChild()
obChild.methodBase()