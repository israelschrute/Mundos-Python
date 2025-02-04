#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo,
#qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
homemmaisvelho = 0
maioridadehomem = 0
mulheres20 = 0
for c in range(1, 5):
    print('***** {}ª Pessoa *****'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    print('')
    somaidade = somaidade + idade
    midade = somaidade / c
    if c == 1 and sexo == 'M':
        homemmaisvelho = nome
        maioridadehomem = idade
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        homemmaisvelho = nome
    if sexo == 'F' and idade < 20:
        mulheres20 += 1

print('A média das idades fornecidas é: {}'.format(midade))
print('O nome do homem mais velho é {} e ele tem {} anos de idade'.format(homemmaisvelho , maioridadehomem))

#Segunda parte: preciso relacionar nome com idade e sexo de forma que, dentre os inputs dado eu
#segregue aquele que for: homem, maior idade e o nome dele.

'''Começo o programa colocando 'if c == 1' e mvhomem = nome. Isso significa que, como eu coloquei somente uma entrada homemmaisvelho,
automaticamente aquele nome é o mais velho ou mais novo. Preciso adicionar o 'and' no intuito de segregar só os nomes associado ao Sexo
masculino.'''
'''Seguindo com o programa eu adiciono:
 if sexo == 'M' and idade > maioridadehomem:
    maioridadehomem = idade
    homemmaisvelho = nome
Eu estou indicando que SE as próximas entradas, após aquele c == 1 tiver idade maior que aquela já acumulada com a primeira entrada. Essa segunda, terceira, quarta ...
entrada passará a assumir aquela posição de maior idade e o nome atrelado.'''
