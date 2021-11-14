arr = [int(elem) for elem in input().split()]
elem = 1

for i in range(arr[0]):
    result = []
    for j in range(arr[1]):
        result.append(elem)
        if elem >= arr[1]:
            elem = 1
        else:
            elem += 1
    print(*result)
    if elem >= arr[1]:
        elem = 1
    else:
        elem = result[0] + 1
        