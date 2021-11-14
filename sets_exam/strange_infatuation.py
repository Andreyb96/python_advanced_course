arr1 = {int(elem) for elem in input().split()}
arr2 = {int(elem) for elem in input().split()}

if len(arr1.intersection(arr2)) == 0:
    print('BAD DAY')
else:
    print(*sorted(arr1.intersection(arr2), reverse=True))
