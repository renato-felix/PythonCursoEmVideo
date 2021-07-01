num = int(input('Digite aqui um, número para saber o seu fatorial: '))
fatorial = num
while num != 1:
    num = num - 1
    fatorial = fatorial * num
print(fatorial)