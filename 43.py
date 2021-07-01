print('Bora calcular seu IMC?')
peso = float(input('Digite aqui o seu peso: '))
altura = float(input('Digite aqui sua altura'))
imc = peso / (altura * altura)
print('Seu IMC é de {:.2f} e você está com '.format(imc), end='')
if imc < 18.5:
    print('o peso abaixo do ideal.')
elif 18.5 <= imc <= 25:
    print('o peso ideal.')
elif 25 < imc <= 30:
    print('sobrepeso')
elif 30 < imc <= 40:
    print('obesidade')
else:
    print('obesidade mórbida')
