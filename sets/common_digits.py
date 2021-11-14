n = int(input())

for i in range(n):
    if i == 0:
        set1 = set([int(elem) for elem in input()])
    else:
        set1.intersection_update(set([int(elem) for elem in input()]))


print(*sorted(set1))
