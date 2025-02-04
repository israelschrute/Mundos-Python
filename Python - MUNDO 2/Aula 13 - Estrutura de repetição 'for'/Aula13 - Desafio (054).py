from datetime import date

atual = date.today().year

menores = 0
maiores = 0

for c in range (1, 8):
    ano = int(input('Qual a data de nascimento da {}ª pessoa? '.format(c)))
    idade = atual - ano
    if idade < 21:
        menores += 1 #Essa parte está fazendo o ACUMULADOR 'menores' receber um 'check' toda vez que o condicional for obedecido
    elif idade >= 21:
        maiores += (idade >= 21) #pra ser mais intuitivo pode escrever assim tb.
print('Dentre as {} pessoa(s), existem {} pessoa(s) menor(es) e {} maior(es) de idade'.format(c, menores, maiores))
