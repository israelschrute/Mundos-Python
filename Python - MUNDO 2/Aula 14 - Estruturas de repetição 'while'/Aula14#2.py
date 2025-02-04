import random

'''for c in range(1, 11):
    print(c)
print('Fim')'''

'''c = 1 #Contador começa no 1
while c < 10: #enquanto o contador for menor do que 10
    print(c)
    c = c + 1
print('End')'''

'''x = random.randint(1, 11)
c = 1
while c < x:
    c = c + 1
    print(c)
print('End')'''

'''for c in range(1, 4):
    n = int(input('Digite um número: '))
    print(n)
print('End')'''

'''n = 1
while n != 0: #Esse (n != 0) é chamado de 'flag' ou 'condição de parada'
    n = int(input('Digite um número: '))
print('End')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('End')'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} impares'.format(par, impar))
