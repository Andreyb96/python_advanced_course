n = int(input())

coords = [input().split() for i in range(n)]

for elem in coords:
    print(*elem)

print()

coords = [i for i in coords if int(i[1]) > 3]

for elem in coords:
    print(*elem)
