n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())

for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j], arr[n-1-j][i] = arr[n-1-j][i] , arr[i][j]
            break
for i in range(n):            
    print(*arr[i])
    