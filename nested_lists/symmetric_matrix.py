def IsSymmetric(arr):
    for i in range(n):
        for j in range(n):
            if i !=j:
                if arr[i][j] != arr[j][i]:
                    return 'NO'
    return 'YES'

n = int(input())
arr = []

for i in range(n):
    arr.append(input().split())
    
print(IsSymmetric(arr));
