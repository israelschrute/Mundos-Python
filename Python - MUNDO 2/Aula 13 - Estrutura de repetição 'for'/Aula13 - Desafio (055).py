'''lista = [] #criando uma lista vazia
for c in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(c)))
    lista.append(peso) #Append = acrescentar à uma lista
print('O peso máximo foi {}Kg e o mínimo foi {}Kg'.format(max(lista), min(lista)))'''

#Ele não ensinou, até aqui, essa função append. Porém ele incentiva a buscar em outros locais.
##basta não copiar e colar o código

pmaior = 0
pmenor = 0

for p in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(p)))
    if p == 1:
        pmaior = peso
        pmenor = peso #Se é o primeiro que eu li, então nem um nem outro é maior ou menor
    else:
        if peso > pmaior: #se os valores de pesos inserido adiante forem maiores que o até então maior peso 'pmaior'
            pmaior = peso #O maior peso se torna agora esse novo input de peso
        if peso < pmenor:
            pmenor = peso
print('O maior peso lido foi de {}Kg'.format(pmaior))
print('O menor peso lido foi de {}Kg'.format(pmenor))
