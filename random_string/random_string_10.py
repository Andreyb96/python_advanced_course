import random

arr = [str(i).ljust(3) for i in range(1,76)]

result = random.sample(arr, 25)
result[12] = '0'.ljust(3)

for i in range(5):
    print(' '.join(result[i*5:i*5+5]))
