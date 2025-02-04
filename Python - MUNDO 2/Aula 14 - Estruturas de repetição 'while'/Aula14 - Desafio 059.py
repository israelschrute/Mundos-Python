print('='*22)
print('Analizador de números')
print('='*22)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

print('O que deseja fazer? ')
print('[1] = Somar\n[2] = Multiplicar\n[3] = Qual é maior?\n[4] = Digitar novos números\n[5] = Sair')
print('')

esc = int(input('Escolha uma das 5 opções acima: '))

if esc == 1:
    soma = n1 + n2
    print('A soma entre {:.1f} e {:.1f} é: {:.2f}'.format(n1, n2, soma))
if esc == 2:
    mult = n1*n2
    print('A multiplicação entre {:.1f} e {:.1f} é: {:.2f}'.format(n1, n2, soma))
if esc == 3:
    if n1 > n2:
        print('O primeiro é maior')
    elif n1 == n2:
        print('Os números são iguais')
    else:
        print('O segundo é maior')
while esc == 4:
    n1 = float(input('Digite seu novo primeiro número: '))
    n2 = float(input('Digite seu novo segundo número: '))
    esc = int(input('Escolha novamente uma das 5 opções acima: '))
    if esc == 1:
        soma = n1 + n2
        print('A soma de {} e {} é: {:.2f}'.format(n1, n2, soma))
    if esc == 2:
        mult = n1*n2
        print(mult)
    if esc == 3:
        if n1 > n2:
            print('O primeiro é maior')
        elif n1 == n2:
            print('Os números são iguais')
        else:
            print('O segundo é maior')
print('')
if esc == 5:
    print('Até mais!')
