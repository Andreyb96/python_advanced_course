n = int(input())
m = int(input())

arr = []
counter = 0

for i in range(n*m):
    if i%m == 0:
        arr.append([input()])
    elif i%m == m-1:
        arr[counter].append(input())
        counter += 1
    else:
        arr[counter].append(input())

for i in range(n):
    print(*arr[i])
