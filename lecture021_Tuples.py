tupleNumbers = (1, 2, 3, 4) #as tuplas utilizam parentezes
print(tupleNumbers)

print()

tupleNumbersAndWords = (1, 'python', 2, 'stranger things', 3.14)
print(tupleNumbersAndWords)

#TUPLAS SAO CONSTANTES. VOCE NAO PODE MUDAR OS VALORES DO INDICE
print('\n\n\n')

print(help(tuple)) #para saber os metodos que pode ser trabalhado de uma classe
                   #so utilizar o metodo "help()"

print()

tupleCount = (1, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6)
print(tupleCount,'\nHow many times can you see (number 4) in this array?\n', 'I can see {} times'.format(tupleCount.count(4)))

print()

tupleIndex = ('Bruno', 'Galya', 'Valentina', 'Ivete')
print(tupleIndex, "\nWhich is the Galya's index?\n", " Galya's index is number {}.".format(tupleIndex.index('Galya')))
