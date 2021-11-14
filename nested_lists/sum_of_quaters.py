n = int(input())
arr = []
maximum = -100;

for i in range(n):
    arr.append([int(i) for i in input().split()])

sumArr = [0]*4
    
for i in range(n):
    for j in range(n):
        if (i<j and i < n-1-j):
            sumArr[0] += arr[i][j]
        elif (i<j and i > n-1-j):
            sumArr[1] += arr[i][j]
        elif (i>j and i > n-1-j):
            sumArr[2] += arr[i][j]
        elif (i>j and i < n-1-j):
            sumArr[3] += arr[i][j]

print('Верхняя четверть: ' + str(sumArr[0]))
print('Правая четверть: ' + str(sumArr[1]))
print('Нижняя четверть: ' + str(sumArr[2]))
print('Левая четверть: ' + str(sumArr[3]))
