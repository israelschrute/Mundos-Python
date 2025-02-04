print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')

for c in range (0, 5):
    print('Hello') #1ª Tabulação do 'for'
print('Fim') #Final do programa, não faz parte da tabulação

for c in range (0, 5): #A letra 'c' para representar esse Laço, esse Sistema, de repetição é uma convenção
    print(c)
print('Fim')

for c in range (0, 5, -1): #Contar de tras pra frente. Especifico na ultima virgula a ITERAÇÃO
    print(c)
print('Fim')

for c in range (0, 10, 2): #Contar de 2 em 2
    print(c)
print('Fim')

idade = int(input('Digite uma idade'))
for c in range (0, 5):
    if idade == 25:
        print('Parado')
    print('Pule')
    print('Corra')
print('End')
