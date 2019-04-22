import numpy as np

original_array=[1,2,3]      #list
a=np.array([1,2,3])         #numpy.ndarray

print(a)                    #will be printed without comma
print(original_array)       #will be printed with comma

print(type(a))              #numpy.ndarray
print(type(original_array)) #list

a2d=np.array([[1,2,3],[3,4,5]])         #numpy.ndarray  2D
a2d1=np.array([[1,2,3],[3,4]])         #numpy.ndarray   1D
print(a2d)
print(a2d1)

aarr=np.arange(0,100)
print(aarr)

element=aarr[6]
print(type(element))        #numpy.int32    Datatype
print(type(element+7))      #numpy.int32    Datatype
print(type(8+7))            #int            Datatype

aarr2D=np.zeros((5,10))
print(aarr2D)

vector=np.linspace(0,20,5)      #start,stop,step
print(vector)
vector=np.linspace(0,20,6)      #start,stop,step
print(vector)

#--------------
a=np.zeros(8)
print(a)                    #in a single line
a=a.reshape((2,2,2))        #with array representation
print(a)
print(a.ravel())

aarr=np.arange(0,100)
print(aarr)
arr_slice=slice(1,10,4)
print(arr_slice)
print(aarr[5:])

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1[0:3,0:1])        #slicing 3 rows, 1 column

print(arr1.shape)
print(arr1.ndim)
print(arr1.itemsize)

arrEmpty=np.empty([3,2],dtype=int)
print(arrEmpty)

np.savetxt("arr.txt",aarr)

newarr=np.loadtxt("arr.txt")
print(newarr)

np.savetxt("arr1.csv",aarr,delimiter=',')
print(np.genfromtxt("arr1.csv",delimiter=','))  #Load/Read file