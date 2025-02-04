somaidade = 0
maioridadehomem = 0
nomomaisvelho = ''
totmulher20 = 0
for p in range(1, 4):
    print('===== {}ª Pessoa ====='.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade #O acumulador sempre vai receber o somatório daquilo que foi inputado ou quand o condicional IF for obedecido
    média = somaidade / p
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
print('A média das idades fornecidas é de {:.2f} anos'.format(média))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomemaisvelho))
print('Nessa lista, existem {} mulheres com menos de 20 anos'.format(totmulher20))
