list = [1, 2, 3, 4]
for i in list:
    print(i, end= " ")

listFind = [1, 20, 3, 4]
find = 10
for i in listFind:
    if i == find:
        print('Good job')
else:
    print('\n\nThe number did not found. Try again.')

print('\n')

for i in range(11): #imprime numeros de 1 ate 10
    print(i, end=' ')

print('\n')

for i in range(6, 10):#imprime intervalo de 6 ate 9
    print(i, end=' ')

print('\n')

for i in range(2, 22, 2): #imprime numeros pares em um intervalo de 2 ate 10
    print(i, end=' ')

print('\n')

name = 'python'
for word in name:
    print(word, end=' ')
    