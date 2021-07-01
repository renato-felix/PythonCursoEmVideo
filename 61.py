a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite qual vai ser a razão dessa P.A.: '))
an = a1
print((a1), end=' ')
while an != a1 + (9 * r):
    an = an + r
    print((an), end=' ')