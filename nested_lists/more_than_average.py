n = int(input())
arr = []

for i in range(n):
    arr.append([int(i) for i in input().split()])
    average = sum(arr[i]) / len(arr[i])
    print(len([elem for elem in arr[i] if elem > average]))
    