soma = 0 # Ajuda muito definir o acumulador antes
cont = 0 # O contador também
for c in range(1, 6):
    num = int(input('Digite o {} valor: '.format(c)))
    soma = soma + num
    cont = cont + 1
print('Foram informados {} valores e a soma desses valores resulta em {}.'.format(cont, soma))
