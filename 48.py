#Não consegui fazer isso sozinho
soma = 0 #Acumulador (Eu não fazia ideia disso...)
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(cont, soma)
#esse exercício eu passei perrengue