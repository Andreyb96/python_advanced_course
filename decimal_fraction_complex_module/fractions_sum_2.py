from fractions import Fraction

def factorial(i):
    if i <=1:
        return 1
    else:
        return factorial(i - 1) * i

summa = Fraction(0)
n = int(input())

for i in range(1, n+1):
    summa += Fraction(1, factorial(i))    
print(summa)
