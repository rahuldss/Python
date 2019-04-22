import matplotlib.pyplot as plt
import numpy

#1.
# y = numpy.random.randn(40,2)
# plt.hist(y)
# plt.show()

#2.
# plt.bar([1,2,6],[2,3,5])
# plt.show()

#3.
# d={'a':25,'b':35,'c':45}
# for i,key in enumerate(d):
#     print(i,key)
#     plt.bar(i,d[key])

# plt.legend()
# plt.xticks(numpy.arange(len(d)),d.keys())
# plt.show()

#4.
# plt.figure(figsize=(3,3))
# plt.pie([40,24,5,28],labels=['c#','Python','Java','C++'])
# plt.show()

#5.
# x=numpy.random.randn(20)
# y=numpy.random.randn(20)
# plt.scatter(x,y)
# plt.savefig('Graph_scatter1.png')
# plt.show()

#6.
x=numpy.arange(1,3)
plt.plot(x,'--')    #Line Type --
plt.plot(x**2,'m')  #Line Color m
plt.plot(x**3,'*')  #Type of Symbol
plt.show()
