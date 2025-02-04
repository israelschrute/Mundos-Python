print('\033[0;31;43mOlá, mundo!\033[m')
print('\033[7;33;44mOlá, mundo!\033[m')

a = 5
b = 3
print('Os valores são: \033[4;35;46m{}\033[m e \033[7;31;47m{}\033[m'.format(a, b))


nome = 'Israel'
print('Olá, prazer em te conhecer {}{}{}!!!'.format('\033[0;31;43m', nome, '\033[m'))


cores = {'Limpa':'\033[m', 'azul':'\033[0;34m', 'amarelo':'\033[0;33m'}
print('Olá, prazer em te conhecher {}{}{}'.format(cores['azul'], nome, cores['Limpa']))
