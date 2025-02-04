print('{:*^40}'.format(' CALCULADORA DE PREÇO '))
print('')
print('Formas de pagamento:\n\n [DINHEIRO/CHEQUE]  = 1\n [CARTÃO A VISTA]   = 2\n [CARTÃO PARCELADO] = 3')
print('')

preço = float(input('Informe o valor das compras: R$'))
forma = int(input('Digite a forma de pagamento: '))

if forma == 1:
    desc1 = preço - (preço*10)/100
    print('O valor final, com desconto, será de R${}'.format(desc1))

elif forma == 2:
    desc2 = preço - (preço*5)/100
    print('O valor final, com desconto, será de R${}'.format(desc2))

elif forma == 3:
    parc = int(input('Quantas parcelas? ')) #sempre que precisar abrir um input dentro de um elif, sobe uma indendação
    if parc <= 2:
        print('Sem desconto, preço normal de R${}'.format(preço))
    elif parc > 2:
        jur = preço + (preço*20)/100
        print('Sua parcela será de R${}'.format(jur/parc))
        print('O valor será acrescido de 20% de juros e passará a ser R${}'.format(jur))
else:
    print('Opão inválida')
    
