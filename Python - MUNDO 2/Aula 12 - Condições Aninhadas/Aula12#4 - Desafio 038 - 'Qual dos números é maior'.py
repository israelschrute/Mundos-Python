print('Olá, bem vindo ao comparador de números')
n1 = int(input('Digite seu primeiro número: '))
n2 = int(input('Digite seu segundo número: '))

if n1 == n2:
    print('Os dois números fornecidos são iguais, não existe valor maior')
elif n1>n2:
    print('O primeiro número {} é maior do que o segundo {}'.format(n1, n2))
elif n2>n1:
    print('O segundo número {} é maior do que o primeiro {}'.format(n2, n1))
