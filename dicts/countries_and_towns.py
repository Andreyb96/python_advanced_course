n = int(input())
result = {}

for i in range(n):
    arr = input().split()
    for j in range(1, len(arr)):
        result[arr[j]] = arr[0]
        
m = int(input())

for i in range(m):
    print(result[input()])
    