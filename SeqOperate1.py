list=['hadoop','bigdata','python']

print(list[1])      #First
print(list[0:2])    #one to two
print(list[-1])     #Last
print(list[-2])     #second Last
print(list[-3])     #third Last

print(list + ['react','android'])
print(list * 3)
print('hadoop' in list,'xyz' in list)

del(list[1])
print(list)

list.append('C Sharp')
print(list)

list.extend(['g','h'])
print(list)

print(list.remove('g'))
print(list.pop(3))
print(list)
print(sorted(list))
print(list[::-1])
#print([x**2 for x in [1,2,3,4,5]])

tup=([0,1,2],[1,2,3],[3,4,5,6])
tup[0][0]='Updated'
print(tup)
