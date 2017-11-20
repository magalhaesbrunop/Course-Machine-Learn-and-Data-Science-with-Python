list = [2, 20, 5, 30, ['joao', 'maria', 'carlota']]
print(len(list))
print(list)
print(list[-1])
print(list[-1][0])
print(list[-1][2])
list[-1][1] = 'Jennifer Lowrence == Gostosa'
print(list[-1][1])
print(list[-1])

print('\n')

list = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
count = 0
while count < len(list):
    print(list[count], end= ' ')
    count += 1
print('\n')
print(list[0:3], '\n')
print(list[3:])
print(list[-3:])

print('\n')

list1 = [1, 20, 2, 30, 3, 40]
list2 = list1
list2[0] = 10
print(list1)

print('\n')

list1 = [1, 20, 2, 30, 3, 40]
list2 = list1[:]
list2[0] = 10
print(list1)
print(list2)

print('\n')

list = [1, 2, 3]
list.append('Bruno')
print(list)

list2 = [4, 5, 6]
contatenated = list + list2
print(contatenated)

contatenated.pop(3)
print(contatenated)

contatenated.remove(5)
print(contatenated)
