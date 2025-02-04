import random
from time import sleep
print('Jokenpo contra a máquina')

PC = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
EU = str(input('Pedra, papel ou tesoura? ')).strip()
EU = EU.upper()
print('')

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')

print('')
if EU == 'PEDRA' and PC == 'PEDRA':
    print('Deu empate, vai de novo!')
elif EU == 'PEDRA' and PC == 'PAPEL':
    print('Você foi embrulhado, PC ganhou!')
elif EU == 'PEDRA' and PC == 'TESOURA':
    print('Você esmagou o PC, você ganhou!')
elif EU == 'PAPEL' and PC == 'PAPEL':
    print('Deu empate, vai de novo!')
elif EU == 'PAPEL' and PC == 'PEDRA':
    print('Você embrulhou o PC, você ganhou!')
elif EU == 'PAPEL' and PC == 'TESOURA':
    print('Você foi picotado, PC ganhou!')
elif EU == 'TESOURA' and PC == 'TESOURA':
    print('Deu empate, vai de novo!')
elif EU == 'TESOURA' and PC == 'PAPEL':
    print('Você picotou ele, você ganhou!')
elif EU == 'TESOURA' and PC == 'PEDRA':
    print('Você foi esmagado, PC ganhou')

print('')
print('A escolha do PC foi: {}'.format(PC))
