import numpy as np

n = int(input())
m = int(input())

arr = []

for i in range(n):
    arr.append(input().split())

idxs = input().split()

arr = np.array(arr) 
arr[:,[int(idxs[0]),int(idxs[1])]] = arr[:,[int(idxs[1]),int(idxs[0])]]

for i in range(n):
    print(*arr[i])
    