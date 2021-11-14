n = int(input())
result = {}

for i in range(n):
    arr = input().split()
    result[arr[0]] = arr[1]
    result[arr[1]] = arr[0]
    
print(result[input()])
