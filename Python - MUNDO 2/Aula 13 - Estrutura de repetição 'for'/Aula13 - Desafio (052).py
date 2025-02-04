n1 = int(input('Digite um número inteiro qualquer: '))
tot = 0
for c in range(1, n1+1):
    if n1 % c == 0:
        print('\033[m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')

#saindo do laço

print('\n\033[mO número {} foi divisível {} vezes'.format(n1, tot))
if tot == 2:
    print('Dessa forma, ele É PRIMO')
else:
    print('Por isso ele NÃO É PRIMO')

#primeiro passo: criou o contador de 1 até o número 'inputado'. Isso serve para determinar o limite de testes
##de divisão que faremos logo em seguida.
#segundo passo: criou um condicional IF. O condicional [n1 % c == 0]. Isso significa que: caso n1 = 29
#ele vai fazer 29/1, 29/2, 29/3, ... , 29/29. Toda vez que o resto de cada divisão dessa der zero, ou seja, for divisão inteira
##ele vai pintar de branco. Quando não for divisão inteira, vai pintar de vermelho.
#O acomulador 'tot' foi criado para receber, quantas vezes aquela condição IF foi satisfeita dentro do range.
#sabendo que se for divisivel mais de 2 vezes no total, significa que não é primo.
#para contabilizar e printar o 'tot' você pode sair do laço.


'''if (n1 % 2) != 0 and (n1 % 3) != 0 and (n1 % 5) != 0 and (n1 % 7) != 0 and n1 != 1:
    print('É primo')
else:
    print('Não primo')'''
#Número primo: só é divisível por 1 e por ele mesmo.
#Primeiros números primos: 2, 3, 5, 7, 11
