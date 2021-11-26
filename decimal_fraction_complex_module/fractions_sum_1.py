from fractions import Fraction

summa = Fraction(0)
n = int(input())

for i in range(1, n+1):
    summa += Fraction(1, pow(i, 2))    
print(summa)
