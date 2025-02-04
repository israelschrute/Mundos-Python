#Aula sobre estruturas de controle.
#CONDIÇÕES ANINHADAS = 'colocar uma coisa dentro da outra, encaixando as coisas'
#Podemos colocar estruturas condicionais dentro de estruturas condicinais
#Lembra do exemplo do algoritmo que listava as condições e caminhos de um carro numa bifurcação?

#Agora imagine que, existam mais de 2 caminhos a se seguir, como proceder?
#Conforme aumentamos a quantidade de opções, caminhos a se seguir, o IF e ELSE ja não bastam
#Se o carro não for p/ direita, ele não tem somente a opção da esquerda, agora ele tem mais numa
#a opção do meio. Como representar isso?
#É sempre importante programar vários 'caminhos'
#Após o primeiro IF, você teoricamente deveria escrever uma ação pro ELSE. Porém, em vez de uma ação escrita nesse ELSE
##você escreve um outro IF
##só que em vez de você colocar um IF: --> ELSE: --> IF: --> ELSE:, você comprime esse ELSE/IF do meio para
##ELIF:. Quanto mais possibilidades você tiver, você vai acrescentando mais ELIF:. Dentro de um IF podem ter vários ELIF, mas somente
##um ELSE, ou nenhum ELSE.
