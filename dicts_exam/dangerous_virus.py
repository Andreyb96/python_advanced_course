s = {'write': 'W', 'read': 'R','execute': 'X'}
d = {}

n = int(input())

for i in range(n):
    arr = input().split()
    d[arr[0]] = arr[1:]

m = int(input())

for i in range(m):
    arr = input().split()
    if s[arr[0]] in d[arr[1]]:
        print('OK')
    else:
        print('Access denied')
