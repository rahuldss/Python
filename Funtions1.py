def sum(a,b):
    sum=a+b
    return(sum)

print(sum(5,2))

print(all([True,True,1,2,False]))
print(all([True,True,1,2,True]))
print(any([True,True,1,2,False]))
print(bin(3))

for i in range(0,11):
    print(i,bin(i))

lst=['roti','dal','chawal']
print(type(enumerate(lst)))
print(list(enumerate(lst)))
print(list(enumerate(lst,10)))

a=5
b=10
print(id(a))
print(id(b))

#Multiple parameter function
def multiPara(user,*users):
    print("first user argument: ",user)

    for user in users:
        print("argument from variable length argument: ",user)

multiPara('Admin','user1','user2')

#Multiple type parameter function
def multiParameter(arg1,arg2,arg3,*args,**kwargs):
    print("first normal argument: ",arg1)
    print("second normal argument: ",arg2)
    print("third normal argument: ",arg3)
    print("non keyword argument: ",args)
    print("Keyworded argument: ",kwargs)

multiParameter(1,2,3,4,5,6,7,name='narender',country='India',age=35)
