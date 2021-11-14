s = input()

arr = s.split()
result = []
curIdx = 0

for i in range(len(arr)):
    if i == 0:
        result.append([arr[i]])
    elif arr[i] != arr[i-1]:
        result.append([arr[i]])
        curIdx += 1
    else:
        result[curIdx].append(arr[i])

print(result)
