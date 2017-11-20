import numpy

value = numpy.genfromtxt("file.csv", delimiter=";", skip_header=1)
print(value)