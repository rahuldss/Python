import matplotlib.pyplot as plt
import numpy

#1. Plotting X values
# plt.plot([1,2,3,4,10])
# plt.show()

# #2. Plotting X,Y Values with 2 ways
# y_values=[1,2,3,4,10]
# print([i**2 for i in y_values])
# plt.plot(y_values,[i**2 for i in y_values])
# plt.show()

# plt.plot([i**2 for i in y_values],y_values)
# plt.show()

# #3. Plotting X,Y Values with 2 ways Using Numpy
# x=numpy.arange(0,5,0.01)
# print(x)
# plt.plot(x,[i**2 for i in x])
# plt.show()

# #4. Plotting X,Y Values with multiple lines
# plt.plot([1,2,3,4,10])
# y_values=[1,2,3,4,10]
# plt.plot(y_values,[i**2 for i in y_values])
# plt.plot([i**2 for i in y_values],y_values)
# x=numpy.arange(0,5,0.01)
# plt.plot(x,[i**2 for i in x])
# plt.show()

#5.
y_values=[1,2,3,4,10]
x=numpy.arange(0,5,0.01)
#plt.plot(x,[i**2 for i in x],[1,2,3,4,10],y_values,[i**2 for i in y_values],[i**2 for i in y_values],y_values)
plt.plot([1,2,3,4,10],label='qqq')
y_values=[1,2,3,4,10]
plt.plot(y_values,[i**2 for i in y_values],label='abc')     #add ledengd
plt.plot([i**2 for i in y_values],y_values,label='def')     #add ledengd
plt.legend()
plt.grid(True)
#1.
#plt.axis([1,3,1,5])
#2.
plt.xlim([1,3])
plt.ylim([1,5])

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Learning MatPlotLib')
plt.savefig('myplot.png')
plt.show()
