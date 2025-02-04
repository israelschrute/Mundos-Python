#Desafio 5
n1=int(input('Digite um número: '))
ant=n1-1
suc=n1+1
print('O antecessor de {} é {} e o sucessor é {}'.format(n1,ant,suc))


#Desafio 6
x1=n1*2
x2=n1*3
x3=n1**(1/2)
print( )
print('O dobro de {} é: {}\nO triplo é: {}\nA raiz quadrada é: {}'.format(n1,x1,x2,x3))


#Desafio 7
b1=float(input('Qual foi sua nota no 1º semestre? '))
b2=float(input('Qual foi sua nota no 2º semestre? '))
media=(b1+b2)/2
print( )
print('Sua 1ª nota é: {}, sua 2ª nota é: {} e sua média final é: {}'.format(b1, b2, media))

#Desafio 8
m1=float(input('Qual a sua altura em metros? '))
m2=m1*100
print('Sua altura em metros é: {}, que é {} centrímetros'.format(m1, m2))

#quando você quer que um programa no seu editor de texto pare de funcionar, coloque
## 3 aspas

#Desafio 9
z1=int(input('Digite um número qualquer: '))
z11=1*z1
z12=2*z1
z13=3*z1
z15=5*z1
z19=9*z1

print('n1 x 1 = {}\nn1 x 2 = {}\nn1 x 3 = {}\nn1 x 5 = {}\nn1 x 9 = {}'.format(z11,z12,z13,z15,z19))

#Desafio 10

n1=float(input('Quanto reais você tem na sua carteira? '))
c1 = n1/3.27
print('Você tem: ${}'.format(c1))

#Desafio 11
a1=float(input('Qual a altura da sua parede (m)? '))
l1=float(input('Qual a largura da sua parede (m)? '))

a2=a1*l1
a3=a2/2

print('A área em (m²) da sua parede é: {} metros quadrados e você vai precisar de {} litros de tinta'.format(a2, a3))

#Desafio 12
p1=float(input('Qual o preço do produto (R$)? '))

d1=p1-((5*p1)/100)

print('Com o desconto de 5%, seu produto sai por R${}'.format(d1))

#Desafio 13
p1=float(input('Qual o seu salário (R$)? '))

d1=p1+((15*p1)/100)

print('Seu novo salário será de: R${}'.format(d1))
