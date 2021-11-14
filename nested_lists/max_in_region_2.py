n = int(input())
arr = []
maximum = -100;

for i in range(n):
    arr.append([int(i) for i in input().split()])

for i in range(n):
    for j in range(n):
        if (i>=j and i <= n-1-j) or (i<=j and i>=n-1-j):
            if arr[i][j] > maximum:
                maximum = arr[i][j]
    
print(maximum)
