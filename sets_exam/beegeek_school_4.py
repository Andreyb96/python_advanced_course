arr1 = {elem for elem in input().split()}
arr2 = {elem for elem in input().split()}

print(*sorted(arr1.union(arr2)))
