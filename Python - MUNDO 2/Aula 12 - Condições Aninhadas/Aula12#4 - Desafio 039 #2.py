from time import sleep
from datetime import date

dtatual = date.today().year

print('==================')
print('ALISTAMENTO MILITAR')
print('==================')

nome=str(input('Digite seu nome completo:')).strip().title()
print(nome  + ', seja bem vindo(a) ao alistamento militar.')

idade = int(input('Digite o ano de nascimento:'))
sexo = str(input('Digite o sexo [M/F]:')).strip().upper()

print('PROCESSANDO ...')
sleep(2)

if sexo == 'F':
    print('Você não precisa se alistar.')
elif sexo == 'M':
    if (dtatual - idade) < 18:
        print('Você ainda não tem idade para se alistar.')
        print('Faltam {} anos para você se alistar.'.format((dtatual-idade)-18))
    elif (dtatual - idade) == 18:
        print('Você deve se alistar este ano.')
    elif (dtatual - idade) > 18:
        print('Você já passou do prazo de alistamento.')
        print('Você deveria ter se alistado há {} anos.'.format((dtatual-idade)-18))
        print('Procure a junta militar mais próxima para regularizar sua situação.')


