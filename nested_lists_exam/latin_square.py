import numpy as np

def is_every_digit_in_arr(arr, n):
    for i in range(1, n + 1):
        if i not in arr:
            return False
    return True

def is_latin_square(arr, n):
    result = []
    a_t = np.matrix(arr).transpose().tolist()
    for i in range(n):
        arr[i] = sorted(arr[i])
        if (result != [] and result != arr[i]) or not is_every_digit_in_arr(arr[i], n):
            return 'NO'
        result = arr[i]
    result = []
    for i in range(n):
        a_t[i] = sorted(a_t[i])
        if (result != [] and result != a_t[i]) or not is_every_digit_in_arr(arr[i], n):
            return 'NO'
        result = a_t[i]
    
    return 'YES'

n = int(input())
arr = []

for i in range(n):
    arr.append([int(elem) for elem in input().split()])

print(is_latin_square(arr, n))
