import numpy

array = numpy.array([1, 2, 3])

print(numpy.tile(array, 3), '\n')

#print(numpy.tile(array, 3, axis=0), '\n') The axis do not work here
#print(numpy.tile(array, 3, axis=1), '\n')

array2 = numpy.array([[1,2,3], [4,5,6]])
print(numpy.tile(array2, 2))

