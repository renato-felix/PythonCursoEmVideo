from random import choice
cont = 1
print('-----ADIVINHE O NÚMERO-----')
numhumano = int(input('Faça jua jogada: '))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nummaquina = int(choice(lista))
while numhumano not in lista:
    numhumano = int(input('O limite é até 10. Tente novamente: '))
while numhumano != nummaquina:
    cont = cont + 1
    if numhumano < nummaquina:
        print('Mais...')
    elif numhumano > nummaquina:
        print("Menos...")
    numhumano = int(input('Tente novamente: '))
print('BINGO!')
print('Tentativas: {}.'.format(cont))