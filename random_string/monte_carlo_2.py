import random

n = 10**6       # количество испытаний
k = 0.0
for i in range(n):
    x = random.random()
    y = random.random()
    k += (x * x + y * y < 1.0)
print(4 * k / n)
