def printFirstTribonacciNums(n):
    arr = []
    for i in range(n):
        if i < 3:
            arr.append(1)
        else:
            arr.append(arr[i - 1] + arr[i - 2] + arr[i - 3])
    print(*arr)

n = int(input())

printFirstTribonacciNums(n)
