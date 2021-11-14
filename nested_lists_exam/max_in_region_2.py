n = int(input())
arr = []
maximum = 0

for i in range(n):
    arr.append([int(elem) for elem in input().split()])

for i in range(n):
    for j in range(n):
        if i >= n - 1 - j and arr[i][j] > maximum:
            maximum = arr[i][j]
    
print(maximum)
