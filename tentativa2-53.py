frase = str(input('Digite uma frase para saber se ela um PALÍDROMO: ')).replace(' ','').upper()
invertida = str(frase[::-1])
if frase == invertida:
    print('É um PALÍDROMO!')
else:
    print('Não é um PALÍDROMO!')
print(frase, invertida)