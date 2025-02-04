#Desafio 22
'''nome1=str(input('Digite seu nome completo: '))

mai=nome1.upper()
min=nome1.lower()

print(mai,min)


n1=len(nome1)
n2=nome1.count(' ')

tot=n1-n2
print('Seu nome possui {} sem considerar espaços'.format(tot))


sp=nome1.split() #separar a frase em blocos [0; 1; 2; 3]
n3=sp[0] #selecionar qual bloco
n4=len(n3) #contar (comprimento) somente a strig splitada

print('Seu primeiro nome é: {} e possuí {} letras.'.format(n3,n4))

#Desafio 23

num1=int(input('Digite um número de 0 a 9999: '))


mil=num1//1000
cen=(num1%1000)//100
dez=(num1%100)//10
und=(num1%10)//1

print('Milhar: {}; Centena: {}; Dezena: {} e Unidade: {}'.format(mil, cen,dez,und))


#Desafio 24

cid=str(input('Digite o nome de sua cidade: '))

x1=cid.split() #Divide em bloco
x2=x1[0] #Seleciona o bloco da anterior
x3=x2.find('Santo') #Procura/Conta (faz qlqer coisa) no bloco selecionado

print('Santo = 0, caso contrário, -1')
print(x3)


#Desafio 25

nome=str(input('Digite seu nome: '))

x1=nome.find('Silva')
print('Silva = 0, caso contrário, -1')
print(x1)


#Desafio 26

frs=str(input('Digite uma frase: '))
x0=frs.upper()
x1=x0.count('A')
print('A frase possui: {} letras "A".'.format(x1))

x2=x0.find('A',0,)
print('A letra "A" está na posição: {}'.format(x2))

x3=len(x0)
x4=x0.rfind('A')
print(x4)'''

#Desafio 27

name=str(input('Qual é o seu nome? '))
uname=name.upper()
x1=uname.split()

x2=x1[0]
print('Seu nome é: {}'.format(uname))
print('Primeiro nome: {}'.format(x2))
x4=x1[len(x1)-1]
print('Último nome: {}'.format(x4))
