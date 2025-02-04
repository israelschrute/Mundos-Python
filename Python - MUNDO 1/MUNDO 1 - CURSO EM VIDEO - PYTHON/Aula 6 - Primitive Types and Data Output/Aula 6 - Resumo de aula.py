#Variável é um "espaçinho" na memória do computador que guarda/aloca aquela informação que o input
#enviou

#TIPOS PRIMITIVOS: tipos são valores (informações) manipulados por funções dentro de variáveis.
#em resumo, qual é o tipo de dado que aquela minha variável é? É um texto? É um número? É um
#operador lógico?

#STRING: são sequências de caracteres imutáveis. Juntar duas strings é chamado de concatenar

#PRINCIPAIS TIPOS: int (1, 2, -5) / float (1.233; 4.6) / bool (true or false) / str ('Olá')

n1=int(input('Qual é o seu primeiro número? '))
n2=int(input('Qual é o seu segundo número? '))
soma=n1+n2
#print('A soma entre', n1, 'e', n2, 'é: ', soma) <-- esse é o jeito mais difícil
print('A soma entre {} e {} vale {}'.format(n1, n2, soma)) #aqui eu atribuo valores à {}

#método: saber a natureza de uma Variável

n=input('Digite algo: ')
print(n.isnumeric())
