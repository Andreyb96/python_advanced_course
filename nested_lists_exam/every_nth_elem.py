arr = input().split()
n = int(input())
result = []

for i in range(n):
    result.append([])

for i in range(len(arr)):
    result[i%n].append(arr[i])

print(result)
