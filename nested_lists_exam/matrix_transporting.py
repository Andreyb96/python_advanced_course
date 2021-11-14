import numpy as np

n = int(input())
arr = []

for i in range(n):
    arr.append([int(elem) for elem in input().split()])
    
a_t = np.matrix(arr).transpose().tolist()

for i in range(n):
    print(*a_t[i])
    