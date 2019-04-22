tupple=(1,2,3)
list=[1,2,3]
print(tupple)

#tupple[0]=5      #tupple doesn't support assignment
list[0]=4     #tuple support assignment
print(tupple)
print(list)

print(1 in list)    #False  
print(1 in tupple)  #True

print(sum(tupple))
print(reversed([1,2,3]))
