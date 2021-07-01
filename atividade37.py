num = int(input('Digite um número inteiro: '))
bi = str(bin(num))
octal = str(oct(num))
hexadecimal = str(hex(num))
opcao = int(input("""Digite a opção que deseja converter a base:
1 - Para BINÁRIO
2 - Para OCTAL
3 - Para HEXADECIMAL
"""))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bi[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, octal[2:]))
elif opcao == 3:
    print('{} convertido em HEXADECIMAL é igal a {}'.format(num, hexadecimal[2:]))
else:
    print('Essa opção não é válida. Pressione SHIFT + F10  para tentar novamente')


