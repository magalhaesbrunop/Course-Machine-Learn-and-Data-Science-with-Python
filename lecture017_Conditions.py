idade = 10
idade2 = 59
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

if idade2 >= 18:
    if idade2 >= 60:
        print('Idoso')
    else:
        print('Adulto')
else:
    print('Menor de idade')


option = 2
if option == 1:
    price = 15
elif option == 2:
    price = 20
elif option == 3:
    price = 30

print('The price is {} dollars.'.format(price))