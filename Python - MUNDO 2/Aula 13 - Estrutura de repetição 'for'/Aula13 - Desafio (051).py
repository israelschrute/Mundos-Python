#P.A = (2, 4, 6, 8) ## [4 - 2] = 2
print('='*43)
print(' OS 10 PRIMEIROS TERMOS DE UM P.A QUALQUER')
print('='*43)
print('')

n1 = int(input('Qual o primeiro termo de sua P.A? '))
n2 = int(input('Qual a razão de sua P.A? '))

for c in range(1, 11):
    PA = n1 + (c - 1)*n2 #Fórmula da P.A. Só procurar na internet, não necessáriamente deveria ter deduzido isso.
    print(PA, end=' - ')
print('END')
