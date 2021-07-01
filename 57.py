sexo = ' '
while sexo not in 'MF':
    sexo = str(input('Digite M ou F: ')).upper()
    if sexo not in 'MF':
        print('Opção inválida. Tente novamnte.')
print('Fim')