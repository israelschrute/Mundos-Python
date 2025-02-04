from time import sleep
from datetime import date

atual = date.today().year

print('Olá jovem, bem vindo a página do Exército para o ano de \033[0;31m{}\033[m.'.format(atual))
ano = int(input('Que ano você nasceu? '))
sexo = str(input('Qual o seu sexo? ')).strip()
sexo = sexo.upper()

print('PROCESSANDO ...')
sleep(0.5)

idade = atual - ano


if sexo == 'FEMININO':
    print('Você não tem alistamento obrigatório')
elif sexo == 'MASCULINO':
    if idade == 18:
        print('\033[0;36mVocê se alista esse ano. Procure a unidade de alistamento mais próxima.\033[m')
    elif idade < 18:
        t1 = 18 - idade
        print('Você ainda não atingiu a idade necessária, faltam \033[0;33m{} anos\033[m para o alistamento'.format(t1))
        print('Você deverá se alistar em: {}'.format(ano + 18))
    elif idade >18:
        t2 = idade - 18
        print('Você está atrasado em \033[0;31m{} anos\033[m, deveria ter se alistado em {}'.format(t2, ano + 18))
        print('Se você ainda não se alistou, procure imediatamente uma unidade de alistamento')
