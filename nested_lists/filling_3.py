n = int(input())

for i in range(n):
    result =[]
    for j in range(n):
        if i == j or i == n - j - 1:
            result.append(1)
        else:
            result.append(0)
    print(*result)
    