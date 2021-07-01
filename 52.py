num = int(input('Digite um número para saber se ele é primo: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont = cont + 1
if 1 < cont < 3:
    print('{} é um número primo.'.format(num))
else:
    print('{} não é um número primo'.format(num))
