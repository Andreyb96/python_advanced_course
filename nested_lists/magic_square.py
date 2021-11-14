def IsMagicSquare(arr, n, summa):
    sumDiag1 = 0
    sumDiag2 = 0
    sumCols = [0] * n
    for i in range(n):
        if len(arr[i]) != len(set(arr[i])):
            return False
        if sum(arr[i]) != summa:
            return False
        for j in range(n):
            if arr[i][j] < 1 or arr[i][j] > pow(n, 2):
                return False
            sumCols[j] += arr[i][j]
            if i == j:
                sumDiag1 += arr[i][j]
                sumDiag2 += arr[i][n - 1- j]
                
    if sumDiag1 != summa or sumDiag2 != summa:
        return False
    for i in range(n):
        if sumCols[i] != summa:
            return False
    return True

n = int(input())
arr = []

for i in range(n):
    arr.append([int(elem) for elem in input().split()])

summa = sum(arr[0])
print('YES' if IsMagicSquare(arr, n, summa) else 'NO')
