s = input()

arr = s.split()
result = []
result.append([])

for i in range(len(arr)):
    result.append([arr[i]])
    for j in range(i, len(arr)):
        if (i != j):
            result.append(arr[i:j+1])

result.sort(key=len)        
print(result)
