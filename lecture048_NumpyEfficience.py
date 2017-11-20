def Sum1(x, y):
    sum = 0
    for i in range(x, y+1):
        sum +=i


import numpy

def Sum2(x, y):
    numpy.arange(x, y+1).sum()

import time

start = time.time()
Sum1(1, 100000001)
end = time.time()
print('Runtime of method "for in range()" without NumPy is {}.'.format(end-start))

start = time.time()
Sum2(1, 100000001)
end = time.time()
print('Runtime of method "numpy.arange()" with NumPy is {}.'.format(end-start))