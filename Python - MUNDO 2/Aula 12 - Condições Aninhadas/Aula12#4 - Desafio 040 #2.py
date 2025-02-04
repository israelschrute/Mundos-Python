print('Boletim de notas')

n1 = float(input('Qual a sua nota da P1?'))
n2 = float(input('Qual a sua nota da P2?'))
n3 = float(input('Qual a sua nota da P3?'))

média = (n1+n2+n3)/3

if média < 5:
    print('Sua média foi {} - Situação: \033[0;31mREPROVADO\033[m'.format(média))
elif 5 < média < 6.5:
    print('Sua média foi {} - Situação: RECUPERAÇÃO'.format(média))
elif média >= 6.5:
    print('Parabéns, Sua média foi {} - \033[0;36mAPROVADO\033[m'.format(média))