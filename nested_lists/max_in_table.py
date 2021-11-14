n = int(input())
m = int(input())

indexes = [0]*2
maximum = -100

for i in range(n):
    arr = [int(i) for i in input().split()]
    valueMax = max(arr)
    if valueMax > maximum:
        maximum = valueMax
        indexMax = max(range(len(arr)), key=arr.__getitem__)
        indexes = [i, indexMax]
    
print(*indexes)
