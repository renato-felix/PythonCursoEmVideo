nome = ''
lista = []
while nome != 'Fim':
    nome = str(input('Digite uma nome para adicionar à lista: '))
    lista.append(nome)
print(lista[0:(len(lista) -1)])