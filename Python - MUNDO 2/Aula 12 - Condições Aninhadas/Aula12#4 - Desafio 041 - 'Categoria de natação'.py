from datetime import date
atual = date.today().year

print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
ano = int(input('Digite seu ano de nascimento: '))

idade = atual - ano
print('Você tem {} anos de idade'.format(idade))

if idade <= 9:
    print('Sua categoria é MIRIN')
elif 9 < idade <= 14:
    print('Sua categoria é INFANTIL')
elif 14 < idade <= 19:
    print('Sua cqategoria é JUNIOR')
elif idade == 20:
    print('Sua categoria é SÊNIOR')
elif idade > 20:
    print('Sua categoria é MASTER')
