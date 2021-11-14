def is_symmetric(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[n-j-1][n-i-1]:
                return 'NO'
    return 'YES'

n = int(input())
arr = []

for i in range(n):
    arr.append([int(elem) for elem in input().split()])

print(is_symmetric(arr, n))
