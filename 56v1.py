acumulador = 0
cont = 0
maior = 0
for pessoas in range(1, 5):
    nome = str(input('Qual o nome da pessoa? ').upper())
    idade = int(input('Qual a idade? '))
    sexo = str(input('Digite M para masculino ou F para feminino: ').upper())
    acumulador = acumulador + idade
    media = acumulador / pessoas
    if idade > maior and sexo == 'M':
        maior = idade
        nome2 = nome

    if sexo == 'F' and idade < 20:
        cont = cont + 1

print('A média de idade é de {}'.format(media))
if maior != 0:
    print('O Homem mais velho tem {} anos e seu nome é {}.'.format(maior, nome2))
else:
    print('O grupo não tem homens')
print('O grupo tem {} mulheres com menos de 20 anos'.format(cont))