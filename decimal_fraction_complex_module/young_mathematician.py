from math import gcd
from fractions import Fraction

n = int(input())

for i in range(1, n//2+1):
    if gcd(i, n - i) == 1:
        result = Fraction(i, n-i)
print(result)
