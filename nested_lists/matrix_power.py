def MatrixMultiply(arr1, arr2, n):
    prod = []
    for i in range(n):
        prod.append([])
        newArr1 = arr1[i]
        for j in range(n):
            newArr2 = [row[j] for row in arr2]
            tmp = 0
            for k in range(n):
                tmp += newArr1[k] * newArr2[k]
            prod[i].append(tmp)
    return prod

def PowerMatrix(arr, power, n):
    if power == 0:
        pass
    elif power == 1:
        return arr
    elif power == 2:
        return MatrixMultiply(arr, arr, n)
    elif power >= 3:
        return MatrixMultiply(PowerMatrix(arr, power - 1, n), arr, n)

n = int(input())
arr = []
prod = []

for i in range(n):
    arr.append([int(elem) for elem in input().split()])

power = int(input())
    
prod = PowerMatrix(arr, power, n)
    
for i in prod:
    print(*i)
    