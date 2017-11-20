print('This is a set')
s = set()
s.add(10)  # aqui o numero 10 aparece pela primeira vez
s.add(20)
s.add(30)
s.add(10)  # aqui pela segunda vez
print(s)  # mas na hora de imprimir, o 10 vai ser impresso somente uma vez

print()


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union = set1.union(set2)

print('This is another sets')
print('',set1, '\n', set2)

print('\nThis is a union of sets')
print(union)

print('\nThis is a intersection of sets')
intersection = set1.intersection(set2)
print(intersection)

print('\nThe difference between sets')
difference = set1.difference(set2)
print(difference)

print()

print('\nSet with repeated elements')
lista = [1, 2, 3, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7]
print(lista)
setList = set(lista)
print('Print only non-repeated elements')
print(setList)
