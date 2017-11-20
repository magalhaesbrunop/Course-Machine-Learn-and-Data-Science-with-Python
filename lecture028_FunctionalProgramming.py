double = lambda x: x * 2
print(double(3))

sum = lambda x, y: x + y
print(sum(10, 20))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter(lambda x: x % 2 == 0, lista)
print(list(filter(lambda x: x % 2 == 0, lista)))
print(list(map(lambda x: x * 2, lista)))
