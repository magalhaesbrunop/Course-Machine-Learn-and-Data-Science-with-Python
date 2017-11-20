list = [20, 30 ,40, 50]
#This slice will print the value on index 1 and
# will end up in the third position on the list
print(list[1:3])

print(list[:2])

print(list[::2])

import numpy
print()
array = numpy.array(list)
print(array)

print(array[1:3])
print(array[:2])
print(array[::2])

print()

list2 = list[:]

list2[1] = 1000

print(list)
print(list2)

print()

bArray = array[:]

bArray[2] = 1000
print(array)
print(bArray)
"""
bArray[:] = 42
print(bArray)
"""
print()

cArray = array.copy()
cArray[3] = 1000
print(array)
print(cArray)