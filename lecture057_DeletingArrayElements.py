import numpy

array = numpy.array([[1,2], [3,4], [5,6]])
arrayPartDeleted = numpy.delete(array, 1, 0)
print('0 - \n', arrayPartDeleted, '\n')

array1 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array1PartDeleted1 = numpy.delete(array1, 0, 1)
print(array1PartDeleted1, '\n')

array2 = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
array2PartDeleted1 = numpy.delete(array2, numpy.s_[::2],0)
print(array2PartDeleted1)