n = int(input())
m = int(input())

arr = []

for i in range(n):
    arr.append([])
    for j in range(m):
        arr[i].append(i*j)

for i in range(n):
    print(' '.join([str(item).ljust(3) for item in arr[i]]))
    