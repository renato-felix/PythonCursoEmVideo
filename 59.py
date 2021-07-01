valor1 = int(input('Primeiro Valor: '))
valor2 = int(input('Segundo Valor: '))
opcao = int(input('''-----Qual a opção?-----
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
'''))
while opcao != 5:
    if opcao == 1:
        print('{} + {} = {}'.format(valor1, valor2, valor1 + valor2))
        opcao = int(input('''----Qual a opção?-----
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA
        '''))
    elif opcao == 2:
        print('{} x {} = {}'.format(valor1, valor2, valor1 * valor2))
        opcao = int(input('''-----Qual a opção?-----
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA
        '''))
    elif opcao == 3:
        if valor1 > valor2:
            print('Entre {} e {}, o valor maior é {}'.format(valor1, valor2, valor1))
        elif valor2 > valor1:
            print('Entre {} e {}, o valor maior é {}'.format(valor1, valor2, valor2))
        else:
            print('Os valores são iguais')
        opcao = int(input('''-----Qual a opção?-----
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA
        '''))
    elif opcao == 4:
        valor1 = int(input('Primeiro Valor: '))
        valor2 = int(input('Segundo Valor: '))
        opcao = int(input('''-----Qual a opção?-----
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA
        '''))
    elif opcao > 5:
        print('Opção inválida. Tente novamnte.')
        opcao = int(input('''-----Qual a opção?-----
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA
        '''))
print('Programa Finalizado')

#Poderia ter sido mais curto hein...
