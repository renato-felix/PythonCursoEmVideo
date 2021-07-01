from datetime import date
sexo = str(input('Tecle F para FEMININO ou M para MASCULINO: ')).lower()
if sexo == 'f':
    print('Você não precisa se alistar')
elif sexo == 'm':
    born = int(input('Digite seu ano de nascimento: '))
    hj = str(date.today())
    anoatual = int(hj[:4])
    idade = anoatual - born

    if idade < 18:
        print('Você tem {} anos de idade. \nPor enquamto você está de boa. \nAinda faltam {} anos para você se alistar, lá em {}'.format(idade, 18 - idade, born + 18))
    elif idade > 18:
        print('Já passou do tempo de se alistar hein...\nVocê já está com {} anos ou vai fazer esse ano ainda.\nDeveria ter se alistado a {} anos, lá em {}.'.format(idade, anoatual - born - 18, born + 18))
    else:
        print('É amigo...Esse ano você faz ou já está com DEZOITÃO.\nCorre lá na junta de serviço militar da sua cidade e faça seu alistamento.')
