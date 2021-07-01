from random import choice
pedra = int(0)
papel = int(1)
tesoura = int(2)
todos = [pedra, papel, tesoura]
escolha = choice(todos)
if escolha == pedra:
    texto1 = str('PEDRA')
elif escolha == papel:
    texto1 = str('PAPEL')
else:
    texto1 = str('TESOURA')
print('JO-KEN-PO')

jogador = int(input(' Faça sua escolha: \n[0] PEDRA \n[1] PAPEL \n[2] TESOURA \nQual das opcões? '))
if jogador == pedra:
    texto2 = str('PEDRA')
elif jogador == papel:
    texto2 = str('PAPEL')
else:
    texto2 = str('TESOURA')
print('Computador escolheu {}. \nJogador escolheu {}.'.format(texto1, texto2))

if escolha == jogador:
    print('EMPATE!!! \n{} e {} se anulam.'.format(texto1, texto2))
elif escolha == pedra and jogador == tesoura:
    print('DERROTA!!! \n{} ganha de {}'.format(texto1, texto2))
elif escolha == pedra and jogador == papel:
    print('VITÓRIA!!! \n {} ganha de {}'.format(texto2, texto1))
elif escolha == papel and jogador == pedra:
    print('DERROTA!!! \n{} ganha de {}.'.format(texto1, texto2))
elif escolha == papel and jogador == tesoura:
    print('VITÓRIA!!! \n{} ganha de {}.'.format(texto2, texto1))
elif escolha == tesoura and jogador == papel:
    print('DERROTA!!! \n{} ganha de {}.'.format(texto1, texto2))
elif escolha == tesoura and jogador == pedra:
    print('VITÓRIA!!! \n{} ganha de {}.'.format(texto2, texto1))




