arr = [int(elem) for elem in input().split()]
flag = False

for i in range(arr[0]):
    result = []
    for j in range(arr[1]):
        if flag:
            result.append('*')
            flag = not flag
        else:
            result.append('.')
            flag = not flag
    print(*result)
    if arr[1]%2 == 0: 
        flag = not flag
