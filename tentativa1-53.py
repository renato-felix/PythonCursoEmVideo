frase = str(input('Digite uma frase para ver ser ela é um palídromo: ')).replace(' ','').upper()
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[letra]
if inverso == frase:
    print('Temos um PALÍDROMO!')
else:
    print('Não temos um PALÍDROMO')