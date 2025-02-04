# [+] = adição / [-] = subtração / [*] = multiplicação / [/] = divisão / [**potência] /
# [//] = divisão inteira / [%] = resto da divisão

n1=5**3
print(n1)

n2='Oi '*7
print(n2)

n3=7+7
print(n3)

#Colocando espaços

#nome=str(input('Qual o seu nome? '))
#print('Seja vem vindo {}'.format(nome))

soma=n1+n3

nome=str(input('Qual o seu nome? '))
print('Seja vem vindo {:>10}!!'.format(nome))
print(nome.isnumeric())
print('É um número? {}'.format(nome.isnumeric()))

print('A soma entre {} e {} é {}'.format(n1, n3, soma))


s1 = 3
s2 = 5
x1 = s1+s2
x2 = s1-s2
x3 = s1*s2
x4 = s1/s2

print('A soma entre {} e {} é {}, a subtração é {}, o produto é {} e a divisão é {}!'.format(s1,s2,x1,x2,x3,x4))

#se eu quiser quebrar meu print uso \n
print('A soma entre {} e {} é {},\n a subtração é {}, o produto é {} e a \n divisão é {}!'.format(s1,s2,x1,x2,x3,x4))
