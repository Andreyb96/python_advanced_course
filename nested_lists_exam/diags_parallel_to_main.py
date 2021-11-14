n = int(input())
arr = []

for i in range(n):
    arr.append([])
    for j in range(n):
        arr[i].append(abs(i-j))

for i in range(n):
    print(*arr[i])
    