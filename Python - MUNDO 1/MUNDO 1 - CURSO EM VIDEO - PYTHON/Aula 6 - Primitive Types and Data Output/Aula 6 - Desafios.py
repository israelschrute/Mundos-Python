algo=input('Digite algo: ')
print(algo)
print(algo.isnumeric())
print(algo.isupper())
print(algo.isalpha())

#ou

print('É um número? {}'.format(algo.isnumeric()))
print('Está em maiúsculo? {}'.format(algo.isupper()))
print('É alfanumérico {}'.format(algo.isalpha()))
