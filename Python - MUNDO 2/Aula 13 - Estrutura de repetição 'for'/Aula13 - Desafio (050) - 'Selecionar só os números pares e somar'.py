s = 0
d = 0
for c in range(0, 6):
    n = int(input('Digite um número qualquer: ')) #Estrutura de repetição
    if (n % 2) == 0: #Estrutura condicional - 'SE o número for par, soma ele'
        s += n
        d += 1 #Significa que 'd' está recebendo so somatório de todos os termos que pertencem ao 'IF' imposto como condicional.
print("Um total de {} números pares entraram na conta e a soma deles é: {}".format(d, s))
