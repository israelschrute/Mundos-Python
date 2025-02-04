#uma cadeia de caracteres nada mais é do que uma frase, em programação: uma string
#Israel é muito lindo é uma cadeia de caracteres, é uma string e sempre vem entre aspas
#mas como manipular essas strings para facilitar a programação?

frase = 'Curso em Vídeo Python'
frase1 = 'Curso em Vídeo Python                  '
#quando eu escrevo dessa maneira, o python coloca essa frase na memória, mas não inteira
##ele cria 'mini espaços' dentre esse espaço da memória com cada caractere, tipo aqueles formulários que preenchemos letra por quadradinho
##cada um desses 'mini espaços', que recebeu um caractere, terá um INDICE
##esse índice vai de 0 até o numero final de caractere
##por conta desse tipo de tratamento, o Python permite fazer manipulação de texto

#FATIAMENTO, um método de manipulação de string
#O colchetes representa um tipo de estrutura de dados no python chamado "Lista"
#Ao colocar entre colchetes o '9' dentro da variável 'frase' eu estou pedindo o caractere no índice 9º

'''frase[9]
frase[9:13]
print(frase[9])

#[9:13] significa que ele vai pegar do índice 9 ao 13, sendo que o 13 não é incluso. O índice inicial é incluso
#esse intervalo que estou 'pegando' chama 'RANGE'
print(frase[9:14])
print(frase[9:21])

#Vou começar no nove, parar no 21, pulando de 2 em 2
print(frase[9:21:2])

#quando eu não coloco o indice inicial, automaticamente iria do índice 0 ao 5 (sendo esse ñ incluso)
print(frase[:5])

#indiquei o início e não indiquei o final, ele automaticamente vai até o último indice e incluí ele
print(frase[15:])

#não especifiquei o 'para no' porque, deixando vazio o argumento do meio, automaticamente o python entende que é do índice
##9 ao último pulando de 3 em 3. '1, 2, 3 (o 3 ele mostra, o 1 e 2 ñ)'
print(frase[9::3])'''

#ANÁLISE DE STRINGS

lenght=len(frase)
print(lenght)

qtdo=frase.count('o')
print(qtdo)

qtd=frase.count('o',0,14)
print(qtd)

fin=frase.find('deo')
print(fin)

exis='Curso'in frase
print(exis)

rep=frase.replace('Python','Android')
print(rep)

up=frase.upper()
print(up)

lo=frase.lower()
print(lo)

cap=frase.capitalize()
print(cap)

tit=frase.title()
print(tit)

#remover espaços excedentes
print(frase1)

stp=frase1.strip()
print(stp)

stpr=frase.rstrip() #espaços a direita começando da direita
print(stp)

stpl=frase.lstrip() #espaços a direita começando da esquerda
print(stp)

sp=frase.split() #dividir em listas a partir dos espaços
print(sp)

jn='-'.join(frase)
print(jn)
