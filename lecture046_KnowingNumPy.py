import numpy

print('Array')
array = numpy.array([10, 20, 30, 40])
print(array)

print('\nArray 2D')
matrix = numpy.array([[1, 2],[3, 4]])
print(matrix)

print('\nAccessing number 4 in array')
print(matrix[1][1])

print('\nAccessing and print each array in different lines')
print(matrix[0,:])
print(matrix[1,:])

print('\nAccessing array by column')
print('First column {}.'.format(matrix[:,0]))
print('Second column {}.'.format(matrix[:,1]))

print('\nTranspose array')
print(matrix.transpose())

print('\nAdding arrays')
array1 = numpy.array([[1, 2], [3, 4]])
array2 = numpy.array([[5, 6], [7, 8]])
print(array1, '\n + \n', array2, '\n = \n', (array1+array2))

print('\nSubtracting arrays')
array1 = numpy.array([[1, 2], [3, 4]])
array2 = numpy.array([[5, 6], [7, 8]])
print(array1, '\n + \n', array2, '\n = \n', (array1-array2))

print('\nMultiplying arrays')
array1 = numpy.array([[1, 2], [3, 4]])
array2 = numpy.array([[5, 6], [7, 8]])
print(array1, '\n + \n', array2, '\n = \n', (array1*array2))

print('\nAdding a array')
array3 = numpy.array([1, 2, 3, 4])
print('The sum of array: {} = {}'.format(array3, array3.sum()))

print('\nIndex max value')
print('The max value of array: {} = {}'.format(array3, array3.argmax()))


print('\nIndex min value')
print('The max value of array: {} = {}'.format(array3, array3.argmin()))
