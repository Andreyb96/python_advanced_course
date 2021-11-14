s = input().split()
arr = []
d = {}

for elem in s:
    if elem in d:
        d[elem] += 1
        arr.append(d[elem])
    else:
        d[elem] = 1
        arr.append(d[elem])

print(*arr)
