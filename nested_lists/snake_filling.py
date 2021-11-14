arr = [int(elem) for elem in input().split()]
elem = 1
isEven = False

for i in range(arr[0]):
    result = []
    for j in range(arr[1]):
        result.append(str(elem).ljust(3))
        if isEven:
            elem -= 1
        else:
            elem += 1
    print(*result)
    if isEven:
        elem += arr[1] + 1
    else:
        elem += arr[1] - 1
    isEven = not isEven
    