from time import sleep
print('Olá, cliente! Qual o seu nome?')
print('')

nome = str(input('Digite seu nome: ')).strip().title()

print('Certo, Sr (a) {}, iremos prosseguir com a análise do seu empréstimo'.format(nome))

valor = float(input('Qual o valor do empréstimo que o Sr (a) deseja? (R$):'))
sal = float(input('Qual o valor do seu salário atual? (R$):'))
parc = int(input('Em quantas parcelas o Sr (a) deseja pagar o empréstimo?'))

print('Analisando...')
sleep(2)

if valor > (2.5*sal):
    print('Desculpe, Sr (a) {}, mas o valor do empréstimo solicitado é maior que 2,5 vezes o seu salário atual. Empréstimo negado!'.format(nome))
else:
    if parc <= 12:
        print('Parabéns, Sr (a) {}, o empréstimo foi aprovado!'.format(nome))
    else: print('Desculpe, Sr (a) {}, mas o número de parcelas solicitadas é maior que 12. Empréstimo negado!'.format(nome))  


