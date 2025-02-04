'''s = 0
for c in range (1, 20, 2): #Vai me gerar números ímpares até 500 (coloquei 20 porque 500 é desnecessário)
    if (c % 3) == 0: #Escolha de somente os múltiplos de 3
        s += (c) #somatório somente dos múltiplos de 3
        print('Os números entre 0 e 500 que são múltiplos de 3 são: {}'.format(c)) #Esse 'c' aqui é diferente do 'c' inicial, pois esse tem um condicional IF
        ##é a história da moedinha. Se no quadradinho tem moeda você pega. Se for multiplo de 3 você contabiliza.
    print(c) #aqui o 'c' não está aninhado no if, logo ele volta a ser o 'c' sem condicional
print('O somatório dos números ímpares que são múltiplos de 3 é: {}'.format(s))'''

s = 0 #Essa técnica de criar uma variável que vai receber uma soma é uma FUNÇÃO ACUMULADORA
cont = 0 #O sinal '+=' significa 'cont recebe cont mais um'
for c in range (1, 501, 2): #Vai me gerar números ímpares até 500 (coloquei 20 porque 500 é desnecessário)
    if (c % 3) == 0: #Escolha de somente os múltiplos de 3
        s += (c) #somatório somente dos múltiplos de 3
        cont += 1
        '''print('Os números entre 0 e 20 que são múltiplos de 3 são: {}'.format(c))'''
print('O somatório dos números ímpares que são múltiplos de 3 é: {}'.format(s))
print('')
print('A quantidade de números ímpares multiplos de 3 é {}'.format(cont))
