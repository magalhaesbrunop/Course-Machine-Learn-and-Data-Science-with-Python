import numpy

"""
value1, value2, value3 = numpy.loadtxt('data.txt', skiprows=0, unpack=True)
print(value1)
print(value2)
print(value3)
"""
value1, value2, value3 = numpy.genfromtxt('data.txt', skip_header=1)
print(value1)
print(value2)
print(value3)
