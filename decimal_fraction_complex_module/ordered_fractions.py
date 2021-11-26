from math import gcd
from fractions import Fraction

n = int(input())
result = []

for i in range(1, n+1):
    for j in range(1, i):
        if gcd(i, j) == 1:
            result.append(Fraction(j, i))
            
for elem in sorted(result):
    print(elem)
