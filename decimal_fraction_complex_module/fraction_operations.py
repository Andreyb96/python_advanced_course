from fractions import Fraction

m = input()
n = input()

print(m + ' + ' + n + ' = ' + str(Fraction(m) + Fraction(n)))
print(m + ' - ' + n + ' = ' + str(Fraction(m) - Fraction(n)))
print(m + ' * ' + n + ' = ' + str(Fraction(m) * Fraction(n)))
print(m + ' / ' + n + ' = ' + str(Fraction(m) / Fraction(n)))
