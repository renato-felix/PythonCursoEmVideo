lista = []
for c in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    lista.append(peso)
print('O menor peso é {}Kg e o maior peso é {}Kg.'.format(min(lista), max(lista)))