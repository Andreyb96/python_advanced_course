size = [int(elem) for elem in input().split()]
arr1 = []
arr2 = []
summa = []

for i in range(size[0]):
    arr1.append([int(elem) for elem in input().split()])

input()

for i in range(size[0]):
    arr2.append([int(elem) for elem in input().split()])
    
for i in range(size[0]):
    summa.append([])
    for j in range(size[1]):
        summa[i].append(arr1[i][j] + arr2[i][j])
        
for i in range(size[0]):
    print(*summa[i])
    