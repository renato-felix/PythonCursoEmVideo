from random import choice
escolha = int(input('''Qual vai ser a sua jogada?
1 - Para ÍMPAR
2 - Para PAR
Digite sua opção: '''))
if escolha == 1:
    jogador = str('ÍMPAR')
    computador = str('PAR')
elif escolha == 2:
    jogador = str('PAR')
    computador = str('ÍMPAR')
else:
    print('Vai dar ruim')
print('Jogador escolheu {} e Computador escolheu {}.'.format(jogador, computador))
jogada = int(input('Digite sua jogada: '))
pcpossibles = [0, 1, 2, 3, 4, 5]
jogadapc = choice(pcpossibles)
print('Computador escolheu {}.'.format(jogadapc))
soma = jogada + jogadapc
if soma % 2 == 0:
    resultado = str('PAR')
else:
    resultado = str('ÍMPAR')
print('A soma dos valores deram {} e venceu quem escolheu {}.'.format(soma, resultado))
if resultado == jogador:
    print('JOGADOR VENCE!')
else:
    print('COMPUTADOR VENCE!')


