sexo = 'M'
sexo = 'F'
while sexo == 'M' or 'F':
    s = str(input('Qual o seu sexo [M/F]? ')).upper()
    if s != 'M' and s != 'F':
        print('Opção inválida, tente de novo.')
