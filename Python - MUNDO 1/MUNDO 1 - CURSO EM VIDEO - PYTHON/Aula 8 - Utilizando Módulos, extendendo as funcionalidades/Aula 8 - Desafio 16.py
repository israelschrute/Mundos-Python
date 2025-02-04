#Desafio 16
import random
import math
n1=float(input('Digite um número qualquer: '))
n2=math.floor(n1)
print('A parte inteira do seu número é: {}'.format(n2))'''

'''#Desafio 17
import math
co=float(input('Digite o Cateto Oposto: '))
ca=float(input('Digite o Cateto Adjacente: '))
soma=co**2+ca**2
hyp=math.hypot(soma)
print('A hipotenusa é: {}'.format(hyp))

#Desafio 18
import math
a1=int(input('Digite o ângulo: '))
sen=math.sin(a1)
cos=math.cos(a1)
tan=math.tan(a1)
print('O seno é: {}, o cosseno é: {} e a tangente é: {}'.format(sen, cos,tan))

#Desafio 19
import random
#podemos criar listas, ou seja, reunir variáveis dentro de um "bloco";
a1=str(input('Digite o nome do primeiro aluno: '))
a2=str(input('Digite o nome do segundo aluno: '))
a3=str(input('Digite o nome do terceiro aluno: '))
a4=str(input('Digite o nome do quarto aluno: '))

lista=[a1, a2, a3, a4]
sor=random.choice(lista)

print('O aluno sorteado foi: {}'.format(sor))

#Desafio 20 - Shuffle = embaralhar

a1=str(input('Digite o nome do primeiro aluno: '))
a2=str(input('Digite o nome do segundo aluno: '))
a3=str(input('Digite o nome do terceiro aluno: '))
a4=str(input('Digite o nome do quarto aluno: '))

lista1=[a1,a2,a3,a4]

sort=random.shuffle(lista1)

print('A ordem de apresentação é: {}'.format(lista1))'''

