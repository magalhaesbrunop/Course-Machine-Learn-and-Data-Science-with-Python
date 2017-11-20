import numpy

array = numpy.array([[1,2,3],[4,5,6]])
print(numpy.array_split(array, 2, axis=0),'\n')

bArray = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(numpy.array_split(bArray,3,axis=0))