termo = int(input('Digite aqui a quantidade de termos da sequência de Fibonacci que deseja ver: '))
t1 = 0
t2 = 1
t3 = t1 + t2
cont = 0
print('{} -> {} -> '.format(t1, t2), end='')
while cont != termo - 2:
    cont = cont + 1
    print((t3), end=' -> ')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
print('FIM')
