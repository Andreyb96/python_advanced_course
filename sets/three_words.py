arr = input().split()

print('YES' if set(arr[0]) == set(arr[1]) and set(arr[0]) == set(arr[2]) else 'NO')
