set1 = set([int(elem) for elem in input().split()])
set2 = set([int(elem) for elem in input().split()])

print(*sorted(set1.difference(set2)))
