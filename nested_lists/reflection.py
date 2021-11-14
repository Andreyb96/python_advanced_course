n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())

for i in range(n//2):
    for j in range(n):
        arr[i][j], arr[n-1-i][j] = arr[n-1-i][j] , arr[i][j]
for i in range(n):            
    print(*arr[i])
    