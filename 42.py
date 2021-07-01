l1 = int(input('Digite o PRIMEIRO  lado: '))
l2 = int(input('Digite o SEGUNDO lado: '))
l3 = int(input('Digite o TERCEIRO lado: '))
if l1 <= l2 <= l3:
    menor = l1
    meio = l2
    maior = l3
elif l2 <= l1 <= l3:
    menor = l2
    meio = l1
    maior = l3
elif l2 <= l3 <= l1:
    menor = l2
    meio = l3
    maior = l1
elif l3 <= l2 <= l1:
    menor = l3
    meio = l2
    maior = l1
elif l3 <= l1 <= l2:
    menor = l3
    meio = l1
    maior = l2
elif l1 <= l3 <= l2:
    menor = l1
    meio = l3
    maior = l2

if menor == meio == maior:
    triangulo = str('EQUILÁTERO')
elif menor == meio != maior or menor == maior != meio or maior == meio != menor:
    triangulo = str('ISÓSCELES')
elif menor != meio != maior != menor:
    triangulo = str('ESCALENO')
if (menor + meio) > maior:
    print('O TRIÂNGULO é possível e ele é {}.'.format(triangulo))
else:
    print('O TRIÂNGULO não é possível.')