import numpy

array = numpy.array([[1,2], [3,4], [5,6]])
print(array[array>3], '\n')

print(array[array<3], '\n')

print(array[array %2 == 0], '\n')

print(array[array %3 == 0], '\n')