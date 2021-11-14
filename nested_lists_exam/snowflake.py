n = int(input())
arr = []

for i in range(n):
    arr.append([])
    for j in range(n):
        if i == n//2 or j == n//2 or i == j or i == n-j-1:
            arr[i].append('*')
        else:
            arr[i].append('.')
            
for i in range(n):
    print(*arr[i])
    