n = int(input())
arr = []
maximum = -100;

for i in range(n):
    arr.append([int(i) for i in input().split()][:i+1])
    if maximum < max(arr[i]):
        maximum = max(arr[i])

print(maximum)
