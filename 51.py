a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
an = 0
n = 0
for c in range(1, 11):
    an = an + 1
    n = n + 1
    pa = a1 + (n - 1) * r
    print(pa)