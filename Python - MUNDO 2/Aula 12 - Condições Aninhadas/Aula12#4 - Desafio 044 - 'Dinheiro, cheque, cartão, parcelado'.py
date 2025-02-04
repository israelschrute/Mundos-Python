print('Calculador de preço')
print('')
print('Formas de pagamento: DINHEIRO/CHEQUE, CARTÃO A VISTA ou CARTÃO PARCELADO')
print('')

preço = float(input('Informe o valor: R$'))
forma = str(input('Digite a forma de pagamento: ')).strip()
forma = forma.upper()

if forma == 'DINHEIRO/CHEQUE':
    desc1 = preço - (preço*10)/100
    print('O valor final, com desconto, será de R${}'.format(desc1))

elif forma == 'CARTÃO A VISTA':
    desc2 = preço - (preço*5)/100
    print('O valor final, com desconto, será de R${}'.format(desc2))

elif forma == 'CARTÃO PARCELADO':
    parc = int(input('Quantas parcelas? ')) #sempre que precisar abrir um input dentro de um elif, sobe uma indendação
    if parc <= 2:
        print('Sem desconto, preço normal de R${}'.format(preço))
    elif parc > 2:
        jur = preço + (preço*20)/100
        print('O valor será acrescido de 20% de juros e passará a ser R${}'.format(jur))

'''if forma == 'DINHEIRO/CHEQUE':
    desc1 = preço - (preço*10)/100
    print('O valor final será de R${}'.format(desc1))
else:
    if forma == 'CARTÃO A VISTA':
        desc2 = preço - (preço*5)/100
        print('O valor final será de R${}'.format(desc2))
    else:
        if forma == 'CARTÃO PARCELADO':
            parc = int(input('Quantas parcelas? '))
        else:
            if parc <= 2:
                print('Sem desconto, preço normal de R${}'.format(preço))
            else:
                if parc > 2:
                    jur1 = preço + (preço*20)/100
                    print(jur1)
                    print('O valor será acrescido de 20% de juros e passará a ser R${}'.format(jur))'''
