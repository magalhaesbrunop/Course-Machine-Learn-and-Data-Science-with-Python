import numpy

matrix1 = numpy.array([[1, 2, 3], [4, 5, 6]])
matrix2 = numpy.array([[7, 8, 9], [10, 11, 12]])

print(numpy.array([matrix1,matrix2]), '\n')

print(matrix2/matrix1, '\n')
print(matrix2*matrix1, '\n')
print(matrix2+matrix1, '\n')
print(matrix2-matrix1, '\n')

print(numpy.matrix.round(matrix2/matrix1), '\n')

print(10*matrix2, '\n')

print(matrix1**3)