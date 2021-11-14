set1 = set([int(elem) for elem in input().split()])
set2 = set([int(elem) for elem in input().split()])
set3 = set([int(elem) for elem in input().split()])

set1.intersection_update(set2)
print(*sorted(set1 - set3, reverse = True))
