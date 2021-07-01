soma = 0 #Acumulador
cont = 0 #Contador
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(cont, soma)
#Não consegui resolver esse...(outra vez...)