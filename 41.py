from datetime import date
nasc = int(input('Digite o ano que você nasceu: '))
anoatual = date.today().year
idade = anoatual - nasc
if idade <= 9:
    print('Esse pivete tem ou ainda vai fazer esse ano {} anos, portanto ele é MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('Esse piá tem ou ainda vai fazer esse ano {} anos, portanto ele é INFANTIL'.format(idade))
elif 14 <idade <= 19:
    print('Esse JOVEM MALDITO tem ou ainda vai fazer esse ano {} anos, portanto ele é JÚNIOR'.format(idade))
elif 19 < idade <= 25:
    print('Esse AINDA FAZ BOSTA tem ou ainda vai fazer esse ano {} anos, portanto ele é um SÊNIOR'.format(idade))
elif 25 < idade <= 100:
    print('Essa VOZ DA SABEDORIA tem ou ainda vai fazer esse ano {} anos, portanto ele é MASTER'.format(idade))
else:
    print('Esse atleta é vivido hein')

