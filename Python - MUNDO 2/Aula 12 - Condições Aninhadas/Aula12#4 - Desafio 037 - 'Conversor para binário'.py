#Conversor de números decimais para 1 - Binário, 2 - Octal e 3 - Hexedecimal
#Conversor Binário
#Exemplo: 25 --> Binário
# 25%2 = 12 com resto = 1
# 12%2 = 06 com resto = 0
# 06%2 = 03 com resto = 0
# 03%2 = 01 com resto = 1
#Quanto chegamos num valor menor que a base (1<2) finalizamos.
#Utilizamos então o último RESULTADO DA DIVISÃO INTEIRA, nesse caso, '1', juntamente com os valores de resto anteriores
#Tudo de trás para frente, dessa forma, 25 = 11001

from time import sleep
print('Olá, bem vindo ao conversor de números!')
print('')
print('OPÇÕES DE CONVERSÃO:\n\n - Binário     = 1\n - Octal       = 2\n - Hexadecimal = 3')
print('')
num = int(input('Digite o número a ser convertido: '))
choice = int(input('Escolha entre as opções de conversão 1 a 3: '))
print('PROCESSANDO ...')
sleep(0.5)

#é importante tirar os dois primeiros dígitos das respostas de conversão, para ficar mais simples, por isso o '[2:]'
if choice == 1:
    print('O número {} convertido para Binário é {}'.format(num, bin(num)[2:]))
elif choice == 2:
    print('O número {} convertido para Octal é {}'.format(num, oct(num)[2:]))
elif choice == 3:
    print('O número {} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
elif choice > 3:
    print('Opção inválida')
