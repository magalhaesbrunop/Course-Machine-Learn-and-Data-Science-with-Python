import numpy

array = numpy.array([1, 2, 3])
arrayMoreValue = numpy.append(array, [4, 5, 6, 7])
print(arrayMoreValue, '\n')

array1 = numpy.array([[1, 2], [3, 4]])
arrayMoreValue1 = numpy.append(array1, [[5, 6]])
print(arrayMoreValue1, '\n')

arrayMoreValue2 = numpy.append(array1, [[5,6]], axis=0)
print(arrayMoreValue2)