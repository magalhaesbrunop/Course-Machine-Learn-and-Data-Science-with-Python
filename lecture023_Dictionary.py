dictionary = {'Bruno':30, 'Galya': 20, 'Ivete':50}
print(dictionary)
print('The age of Bruno is {} years old.'.format(dictionary['Bruno']))
dictionary['Bruno'] = 20
print('Now the age of Bruno is {} years old.'.format(dictionary['Bruno']))
dictionary['Valentina'] = 6
print(dictionary)

for k in dictionary:
    print(dictionary[k], end=' ')

print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())

print('Valentina' in dictionary)
print('Galina' in dictionary)