arr = [int(elem) for elem in input().split()]
elem = 1
for i in range(arr[0]):
    result =[]
    for j in range(arr[1]):
        result.append(elem)
        elem += 1
    print(*result)
    