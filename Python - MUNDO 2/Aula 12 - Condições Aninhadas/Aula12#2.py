#Parte prática
nome = str(input('Qual é o seu nome? ')).strip()
nome2 = nome.upper()
if nome2 == 'ISRAEL':
    print('Que nome esplendoroso!!!')
    print('Tenha um bom dia {}'.format(nome2))
elif nome2 == 'EMILY':
    print('Você é uma cachorrinha linda')
elif nome2 in 'LUCIENE GEORGE HELDER':
    print('Vocês fazem parte da minha familia?')
else:
    print('Seu nome é OK,')
    print('Tenha um bom dia {}'.format(nome2))
