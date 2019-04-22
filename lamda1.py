def ans(z):
    return z*4

print(ans(2))

ans1=(lambda z:z*4)
print(ans1(2))

#map
items=[1,2,3,4,5]
squared=list(map(lambda x:x**2, items))
print(squared)
cubed=list(map(lambda x:x**3, items))
print(cubed)

#filter
numberList=range(-5,5)
less_then_zero=list(filter(lambda x:x<0,numberList))
print(less_then_zero)

#reduce
from functools import reduce
product=reduce((lambda x,y:x*y),[1,2,3,4])
print(product)
product=reduce((lambda x,y:(x+1)*(y)),[1,2,3,4])
print(product)
