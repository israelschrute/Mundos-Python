#instruindo um carro a chegar no ponto B, partindo do ponto A
#Carro = Objeto
#Comandos = carro.siga() - 'siga' é um método e todo método tem '()' no final
#No final do código, observamos que os comandos foram sequenciais, ordenado de cima p/ baixo
#com isso temos uma ESTRUTURA SEQUENCIAL
#Todos os programas até agora foram sequenciais, ou seja, o primeiro a ser executado seguia uma ordem
##de cima p/ baixo. Mas nem sempre será assim, as vezes, para algo acontecer, um código que foi escrito
##depois desse 'algo' precisa ser executado primeiro, com isso acaba essa ideia de 'sequencial'

#Tudo muda se eu tiver mais de uma POSSIBILIDADE de chegar num local B. Por exemplo, posso ir de A até B
##pelo caminho X ou Y
#lembrando que um conjunto de instruções sequenciadas é um: ALGORITMO
#Quando eu tenho duas formas de realizar algo eu tenho que pensar assim: 'Dado que eu tomei tal atitude, agora sigo dessa forma'
#se eu escolhi ir pelo caminho X, não posso seguir a sequencia de Y
#Dentro de um algoritmo, temos sub-algoritmos que descrevem todas as possibilidades para chegar do inicio ao final

#INTRODUZIMOS AQUI O CONCEITO DE 'CONDIÇÕES'

#dentro do conceito de CONDIÇÕES temos uma estrutura importantíssima chamada 'SE' e 'SENÃO'

#lembra que dentro de um algoritmo podemos ter mais de uma possibilidade de sair do início e chegar ao final de um código?
#e que dentro desses algoritmos temos os sub-algoritmos...
#a função SE e SENÃO vem justamente para escolher automaticamente uma dentre varias possibilidade de executar um programa,
#dado que uma informação prévia aconteceu.
#'Dado que o caminho X está engarrafado, siga pelo caminho Y'

#INTRODUZIMOS o conceito de INDENTAÇÃO, apertando [TAB]
#'SE' e 'SENÃO' --> 'if' e 'else'

#Carro Siga()
#se carro.esquerda():
    #carro.siga()
    #carro.esquerda()
#senão:
    #carro.siga()
    #carro.direita()
    #carro.siga()
#carro.pare()

#Temos a separação de blocos: o verdadeiro e o falso, sempre um passo p/ dentro

#por fim, em uma CONDIÇÃO, somente um bloco é executado, nunca os dois


'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--FIM--')'''


#Estruturas condicionais

time=int(input('Qual é o ano? '))
if time>4:
    print('Seu carro é Velho')
else:
    print('Tudo bem')
