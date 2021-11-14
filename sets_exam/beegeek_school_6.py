m = int(input())
resultArr = set()
currArr = set()

for i in range(m):
    n = int(input())
    for j in range(n):
        if i == 0:
            resultArr.add(input())
        else:
            currArr.add(input())
    if i != 0:        
        resultArr = resultArr.intersection(currArr)
        currArr = set()

for elem in sorted(resultArr):
    print(elem)
    