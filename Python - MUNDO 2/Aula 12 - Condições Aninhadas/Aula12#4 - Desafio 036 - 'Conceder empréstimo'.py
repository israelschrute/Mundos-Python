from time import sleep
print('Olá cliente, vamos analisar sua condição de empréstimo')
print('')

valor = float(input('Qual o valor do imóvel? R$'))
sal = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))

print('')
print('PROCESSANDO REQUERIMENTO ...')
sleep(2)

mens = valor/(anos*12) #Parcela mensal. Ficar atendo, eu tinha colocado somente (valor/anos)
limite = (sal*30)/100 #Condição limitadora de 30% do salário

print('A parcela mensal desse financiamento é R${:.2f}'.format(mens))

if mens <= limite:
    print('Você teve seu empréstimo APROVADO, realize seu sonho!')
else:
    print('Infelizmente NÃO podemos te oferecer um empréstimo agora')
