a={1,2,3,4}
b={4,5,6}
print(a|b)  #Union
print(a&b)  #Intersection
print(a-b)  #difference
print(a-(a&b))

a.remove(1)     #Throw error if element is not present
a.discard(1)    #will not throw error if element is not present

person={
    'first_name' : 'Narender',
    'last_name' : 'Sharma',
    'age' : 35,
    'city' : 'Delhi'
}

for item in sorted(person.keys()):
    print(item)
