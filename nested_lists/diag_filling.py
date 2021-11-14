arr = [int(elem) for elem in input().split()]
elem = 1
result = []
sumIdx = arr[0] + arr[1] - 1
d = {}
minimum = min(arr)

for i in range(sumIdx):
    if i < minimum:
        d[i] = [i + 1, 0]
    elif i > sumIdx - minimum:
        d[i] = [sumIdx - i, 0]
    else:
        d[i] = [minimum, 0]

for i in range(arr[0]):
    result.append([])
    for j in range(arr[1]):
        if i+j == 0:
            d[i+j][1] += 1
        elif d[i+j][1] == 0:
            d[i+j][1] = d[i+j-1][1] + d[i+j-1][0] + 1
        else:
            d[i+j][1] += 1
        d[i+j][0] -= 1
        result[i].append(d[i+j][1])

for i in range(arr[0]):        
    print(*result[i])
    