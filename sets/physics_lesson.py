set1 = set([int(elem) for elem in input().split()])
set2 = set([int(elem) for elem in input().split()])
set3 = set([int(elem) for elem in input().split()])

print(*sorted(set3 - set1.union(set2), reverse=True))
