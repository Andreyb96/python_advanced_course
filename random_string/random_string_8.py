import random

arr = [i for i in range(1,10)]

for i in range(100):
    print(''.join([str(i) for i in random.sample(arr, 7)]))
    