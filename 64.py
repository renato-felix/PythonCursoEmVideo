num = int(input('Digite um número: '))
acumulador = 0
cont = 0
while num != 999:
    cont = cont + 1
    acumulador = acumulador + num
    num = int(input('Digite um número: '))
print('Foram digitados {} números e a soma deles é {}.'.format(cont, acumulador))
