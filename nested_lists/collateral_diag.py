n = int(input())

for i in range(n):
    arr = []
    for j in range(n):
        if i == n - j - 1:
            arr.append(1)
        elif i > n - j - 1:
            arr.append(2)
        else:
            arr.append(0)
    print(*arr)
    