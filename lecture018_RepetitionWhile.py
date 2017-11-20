count = 1
while count <= 10:
    print(count, end= ' ')
    count+=1
print('')
count = 2
while count <= 100:
    print(count, end=' ')
    count+=2
    if count == 51:
        print('\n')

print('\n')

multiply = 1
while multiply <= 10:
    number = 1
    while number <= 10:
        print('{} x {} = {}'.format(multiply, number, multiply*number))
        number += 1
    multiply += 1