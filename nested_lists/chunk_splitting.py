s = input()
chunkSize = int(input())

arr = s.split()
result = []
curIdx = 0

for i in range(len(arr)):
    if i == 0:
        result.append([arr[i]])
    elif len(result[curIdx]) < chunkSize:
        result[curIdx].append(arr[i])
    else:
        result.append([arr[i]])
        curIdx += 1

print(result)
