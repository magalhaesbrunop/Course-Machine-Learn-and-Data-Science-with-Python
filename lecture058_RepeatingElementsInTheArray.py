import numpy

array = numpy.array([[1,2], [3,4]])
print(numpy.repeat(array, 4), '\n')

print(numpy.repeat(array,2, axis=0))

print(numpy.repeat(array,2, axis=1))

