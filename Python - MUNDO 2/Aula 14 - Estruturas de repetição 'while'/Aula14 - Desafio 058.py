import random

PC = random.randint(0, 10)
'''print(PC)'''

player = 0
tentativas = 0
while player != PC:
    player = int(input('Digite a sua alternativa entre 0 e 10: '))
    tentativas += 1
    if player == PC:
        print('Você acertou! Para isso, precisou de {} tentativas.'.format(tentativas))
