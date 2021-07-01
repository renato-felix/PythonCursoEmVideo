n1 = float(input('Digite a PRIMEIRA nota: '))
n2 = float(input('Digite a SEGUNDA a nota: '))
media = (n1 + n2) / 2
print('A primeira nota do aluno foi {} e a segunda nota foi {}. Portanto, sua média foi {}.'.format(n1, n2, media))
if media < 5:
    print('REPROVADO')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7 and media <= 10:
    print('APROVADO')
else:
    print('ESSE ALUNO É UM VERDADEIRO ESPETÁCULO')
