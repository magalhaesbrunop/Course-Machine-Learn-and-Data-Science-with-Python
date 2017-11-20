import numpy

joaoPoints = [20, 30, 40, 15]
pedroPoints = [100, 24, 48, 23]
mariaPoints = [92, 22, 34, 12]
marcosPoints = [12, 34, 12, 43]

points = numpy.array([joaoPoints, pedroPoints, mariaPoints, marcosPoints])

print(points)
print()
print(points[2])
print()
print(points[1][0])
print()
print(points.item(5))

print()

myData = numpy.arange(0, 20)
print(myData)
print()

array = numpy.reshape(myData, (5,4))
print(array)
print()
print(array[2,2])
print()

array1 = ['python', 'eh', 'legal']
array2 = ['guido', 'van', 'rossum']
array3 = [10, 20, 30]
print(numpy.array([array1, array2, array3]))

