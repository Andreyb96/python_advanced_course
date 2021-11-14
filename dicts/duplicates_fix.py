arr = input().split()
result = {}
resultArr = []

for elem in arr:
    if elem in result:
        resultArr.append(elem + '_' + str(result[elem]))
        result[elem] += 1
    else:
        resultArr.append(elem)
        result[elem] = 1

print(*resultArr)
