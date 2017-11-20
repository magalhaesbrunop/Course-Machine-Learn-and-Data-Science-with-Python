import numpy

array = numpy.array([[1, 2], [3, 4]])
array2 = numpy.array([[5, 6]]) # as duas matrizes
                               # precisam ter o mesmo
                               # numero de [].

print(numpy.concatenate((array, array2)),'\n')

# Nesse caso tenho que transpor essa matriz para
# poder fazer a concatenação no eixo 1.
print(numpy.concatenate((array, array2.T), axis=1))
