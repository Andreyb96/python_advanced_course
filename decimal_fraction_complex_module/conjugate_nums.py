n = int(input())
z1 = complex(input())
z2 = complex(input())

print(pow(z1, n) + pow(z2, n) + pow(z1.conjugate(), n) + pow(z2.conjugate(), n + 1))
