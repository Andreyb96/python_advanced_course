n = int(input())
d = {}

for i in range(n):
    arr = input().split()
    if arr[0] in d:
        if arr[1] in d[arr[0]]:
            d[arr[0]][arr[1]] += int(arr[2])
        else:
            d[arr[0]][arr[1]] = int(arr[2])
    else:
        d[arr[0]] = {arr[1] : int(arr[2])}
        
for name in sorted(d):
    print(name + ':')
    for product in sorted(d[name]):
        print(product + ' ' + str(d[name][product]))
        