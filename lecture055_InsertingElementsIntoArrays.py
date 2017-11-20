import numpy

array = numpy.array([1, 2, 3])
print(numpy.insert(array, 1, 10), '\n')

arr = numpy.array([[1, 2], [3, 4]])
print(arr, '\n')
print(arr.ndim, '\n')

print(arr.sum(axis=0))
print(arr.sum(axis=1), '\n')

print(numpy.insert(arr, 1, 5, axis=1), '\n')
print(numpy.insert(arr, 0, 5, axis=0), '\n')
