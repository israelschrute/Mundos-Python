frase = str(input('Escreva uma frase: ')).strip().upper()

palavras = frase.split() #precisei 'splitar' para posteriormente 'juntar' sem os espaços entre palavras
junto = ''.join(palavras)
#INFORMAÇÃO IMPORTANTÍSSIMA **** TODO SPLIT DE STRING GERA UMA LISTA **** importante ferramenta
inverso = '' #preciso, agora, ler a strig de trás pra frente
#oloboamaolobo
'''print(len(junto))
print(junto[12])'''

#se você observar, a última letra da frase 'oloboamaolobo' está no índice 12 e não no len = 13.
#dessa forma, eu quero 'ler' essa string por completo, portanto vou do (len -1) até o caractere -1
#-1 porque se fosse até 0, iria cair na letra 'O', mas essa não seria computada. Lembra do conjunto aberto onde caí o indice.
#o ultimo -1 é pra indicar caminho inverso

#escrevendo somente (print(letra)), ele vai escrever o range numeral de tras pra frente.
#escrevendo print(junto[12]) eu estou pedindo 'mostre o índice 12 da string [junto]'
#escrevendo print(junto[letras]) eu estou pedindo 'mostre cada elemento do range criado'
#junto é minha string e letras e minha posição, que assume diferentes valores devido ao laço

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra] #apenas criando um ACUMULADOR que vai receber essa 'leitura inversa'
print(junto, inverso)
if inverso == junto:
    print('As duas palavras SÃO palíndromas')
else:
    print('As duas palavras NÃO SÃO palíndromas')

'''frase = str(input('Escreva uma frase: ')).strip().upper(),
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(junto, inverso)
if inverso == junto:
    print('As duas palavras SÃO palíndromas')
else:
    print('As duas palavras NÃO SÃO palíndromas')'''
