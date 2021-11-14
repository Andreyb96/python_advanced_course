import random

n = int(input())

arr = [input() for i in range(n)]
size = len(arr)
arr += arr


for i in range(size):
    if (arr[i] == arr[size*2 - i - 1]):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr[i] + ' - ' + arr[size*2 - i - 1])
    