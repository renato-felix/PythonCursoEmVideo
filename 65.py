num = int(input('Digite um número: '))
texto = str('S')
lista = []
acumulador = 0
maior = num
menor = num
while num != 0:
    texto = str(input('Deseja continuar? S/N')).upper()
    if texto == 'N':
    lista.append(num)
    acumulador = acumulador + num
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
    num = int(input('Digite um número: '))
media = acumulador/len(lista)
print('Total de números digitados: {} \nSoma dos números digitados: {} \nMédia dos números digitados: {} \nMenor valor: {} \nMaior valor: {}'.format(len(lista), acumulador, media, menor, maior))
print('Programa finalizado.')