a = float(input('Digite o comprimento (cm) da reta 1: '))
b = float(input('Digite o comprimento (cm) da reta 2: '))
c = float(input('Digite o comprimento (cm) da reta 3: '))

x1 = b - c
x2 = a - c
x3 = a - b

#tive que usar '+' para somar condições, vírgulas não funcionam. Posso usar 'and' também
#essa indentação para dentro (IF dentro de um IF) serve quando: "Tal Condição aconteceu e por conta disso
##tenho outras condições seguidas de IF's e ELIF's.
#Essa caso de indentação ocorre normalmente quando, eu tenho, a princípio, somente um IF e else
##nesse caso, PODE ou NÃO PODE formar triângulo. Só que, dentro do 'PODE' eu tenho mais opções, dentro do 'NÃO PODE'
##Eu não tenho mais oções.
##Resumindo: Quando somente uma Condicional do seu código explora outras condições, então use uma indentação pra dentro.

if (abs(x1) < a < (b+c)) and (abs(x2) < b < (a+c)) and (abs(x3) < c < (a+b)):
    print('\033[0;36mÉ possível formar um triângulo\033[m')
    if (a+b) == (a+c) == (b+c):
        print('É um triângulo Equilátero')
    elif (a+b) == (a+c) != (b+c) or (a+b) == (b+c) != (a+c) or (b+c) == (a+c) != (a+b):
        print('É um triângulo Isóceles')
    elif (a+b) != (a+c) != (b+c):
        print('É um triângulo Escaleno')
else:
    print('\033[0;31mNão é possível formar um triângulo\033[m')


'''if (a+b) == (a+c) == (b+c):
    print('É um triângilo Equilátero')
elif (a+b) == (a+c) != (b+c) or (a+b) == (b+c) != (a+c) or (b+c) == (a+c) != (a+b):
    print('É um triângulo Isóceles')
elif (a+b) != (a+c) != (b+c):
    print('É um triângulo Escaleno')'''
