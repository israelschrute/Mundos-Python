from random import choice
from time import sleep

print('Vamos jogar PEDRA, PEPEL ou TESOURA!')
print('')
print('Faça sua escolha com base na lista abaixo:')
print('')

n1 = 'PEDRA'
n2 = 'PAPEL'
n3 = 'TESOURA'

print('[1] = {}, [2] = {} e [3] = {}'.format(n1, n2, n3))
print('')

pc= choice([n1, n2, n3])
escolha = int(input('Digite o número correspondente a sua escolha: '))

print('')
print('Analisando...')
print('')

if pc == n1 and escolha == 1:
    print('Deu empate, o PC escolheu PEDRA!')
elif pc == n1 and escolha == 2:
    print('Você ganhou, o PC escolheu PEDRA!')
elif pc == n1 and escolha == 3:
    print('Você perdeu, o PC escolheu PEDRA!')
elif pc == n2 and escolha == 1:
    print('Você perdeu, o PC escolheu PAPEL!')
elif pc == n2 and escolha == 2:
    print('Deu empate, o PC escolheu PAPEL!')
elif pc == n2 and escolha == 3:
    print('Você ganhou, o PC escolheu PAPEL!')
elif pc == n3 and escolha == 1:
    print('Você ganhou, o PC escolheu TESOURA!')
elif pc == n3 and escolha == 2:
    print('Você perdeu, o PC escolheu TESOURA!')
elif pc == n3 and escolha == 3:
    print('Deu empate, o PC escolheu TESOURA!')
else:
    print('Opção inválida, tente novamente!')
