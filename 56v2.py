acumulador = 0
cont = 0
maior = 0
mulheres = 0
for pessoas in range(1, 5):
    nome = str(input('Qual o nome da pessoa? ').upper())
    idade = int(input('Qual a idade? '))
    sexo = str(input('Digite M para masculino ou F para feminino: ').upper())
    acumulador = acumulador + idade
    media = acumulador / pessoas
    if idade > maior and sexo == 'M':
        maior = idade
        nome2 = nome
    if sexo == 'F':
        cont = cont + 1
        if idade < 20:
            mulheres = mulheres + 1

print('A média de idade do grupo é {}'.format(media))
if maior != 0:
    print('O homem mais velho do grupo se chama {} e tem {} anos.'.format(nome2, maior))
else:
    print('O grupo não tem homens')
if mulheres != 0:
    print('O grupo tem {} mulheres com menos de 20 anos'.format(mulheres))
else:
    print('O grupo não tem mulheres')