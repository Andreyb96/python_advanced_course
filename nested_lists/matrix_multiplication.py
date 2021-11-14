size1 = [int(elem) for elem in input().split()]
arr1 = []
arr2 = []
prod = []

for i in range(size1[0]):
    arr1.append([int(elem) for elem in input().split()])

input()

size2 = [int(elem) for elem in input().split()]

for i in range(size2[0]):
    arr2.append([int(elem) for elem in input().split()])  
    
for i in range(size1[0]):
    prod.append([])
    newArr1 = arr1[i]
    for j in range(size2[1]):
        newArr2 = [row[j] for row in arr2]
        tmp = 0
        for k in range(len(newArr1)):
            tmp += newArr1[k] * newArr2[k]
        prod[i].append(tmp)
        
for i in prod:
    print(*i)
    