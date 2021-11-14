n = int(input())
result = {}

for i in range(n):
    arr = input().split()
    for j in range(0, len(arr) - 1):
        if arr[-1].lower() in result:
            result[arr[-1].lower()].append(arr[j])
        else:
            result[arr[-1].lower()] = [arr[j]]
        
m = int(input())

for i in range(m):
    request = input().lower()
    if request in result:
        print(*result[request])
    else:
        print('абонент не найден')
        