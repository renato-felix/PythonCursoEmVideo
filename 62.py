escolha = int(input('Deseja verificar uma P.A.? \n[1] - SIM \n[0] - NÃO \n'))
while escolha != 0:
    if escolha == 1:
        a1 = int(input('Digite o primeiro termo da P.A.: '))
        r = int(input('Digite qual vai ser a razão dessa P.A.: '))
        n = int(input('Digite até qual termo você quer ver: '))
        an = a1
        cont = 0
        while cont <= n - 1:
            print((an), end=' -> ')
            cont = cont + 1
            an = an + r
        print('Aguardando...')
        termosamais = int(input('Deseja adicionar quantos termos a mais? \n'))
        while termosamais != 0:
            while cont <= n + termosamais - 1:
                print((an), end=' -> ')
                cont = cont + 1
                an = an + r
            termosamais = int(input('Deseja adicionar quantos termos a mais?'))
        escolha = int(input('Deseja fazer mais alguma veficação? \n[1] - SIM \n[0] - NÃO \n'))
    elif escolha > 1:
        escolha = int(input('OPÇÃO INVÁLIDA! \nDeseja fazer mais alguma verificação? \n[1] - SIM \n[0] - NÃO \n'))
print('Programa finalizado com {} termos exibidos'.format(cont))