n = int(input())
arr = []
sum = 0

for i in range(n):
    arr.append([int(i) for i in input().split()])
    sum += arr[i][i]
    
print(sum)
