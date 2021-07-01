from datetime import datetime
ano = datetime.now().year
cont = 0
for c in range(1,8):
    nasc = int(input('Digite o ano de nascimento da pessoa {}:'.format(c)))
    idade = ano - nasc
    if idade < 18:
        cont = cont + 1
        menor = cont
    else:
        cont = cont + 1
        maior = cont
print('{} pessoas são maiores de idade e {} pessoas são menores de idade.'.format(maior, menor))