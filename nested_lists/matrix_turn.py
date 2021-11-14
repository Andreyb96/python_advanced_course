n = int(input())
arr = []
result = []

for i in range(n):
    arr.append(input().split())

for j in range(n):
    result.append([])
    for i in reversed(range(n)):
        result[j].append(arr[i][j])

for i in range(n):
    print(*result[i])
    