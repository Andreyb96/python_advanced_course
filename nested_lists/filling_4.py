n = int(input())

for i in range(n):
    result =[]
    for j in range(n):
        if (i >= j and i >= n - 1 - j) or (i <= j and i <= n - 1 - j):
            result.append(1)
        else:
            result.append(0)
    print(*result)
    