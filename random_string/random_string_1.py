import random

n = int(input())

for i in range(n):
    print('Орел' if random.randint(0,1) == 0 else 'Решка')
