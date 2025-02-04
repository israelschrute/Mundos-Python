print('BOLETIM DE NOTAS')
n1 = float(input('Nota da P1: '))
n2 = float(input('Nota da P2: '))

média = (n1+n2)/2

if média < 5:
    print('Sua média foi {} - Situação: \033[0;31mREPROVADO\033[m'.format(média))
elif 5 < média < 7:
    print('Sua média foi {} - Situação: RECUPERAÇÃO'.format(média))
elif média >= 7:
    print('Parabéns, Sua média foi {} - \033[0;36mAPROVADO\033[m'.format(média))
