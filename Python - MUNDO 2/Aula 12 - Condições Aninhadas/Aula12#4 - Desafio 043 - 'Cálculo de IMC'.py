print('Medidor de IMC')

peso = float(input('Qual o seu peso (Kg)? '))
altura = float(input('Qual a sua altura (m)? '))

IMC = (peso/(altura**2))
print('Seu IMC é: {:.1f}'.format(IMC))

if IMC < 18.5:
    print('Você está abaixo do peso ideal')
elif 18.5 <= IMC <= 25:
    print('Você está no seu peso ideal')
elif 25 < IMC <= 30:
    print('Você está com sobrepeso')
elif 30 < IMC <= 40:
    print('Você está obeso, procure ajuda')
elif IMC > 40:
    print('Você está morbidamente obeso, procure ajuda')
