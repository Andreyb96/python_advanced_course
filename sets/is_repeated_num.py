s = [int(i) for i in input().split()]
arr = set()

for elem in s:
    if elem in arr:
        print('YES')
    else:
        print('NO')
        arr.add(elem)
        