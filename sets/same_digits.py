set1 = set([int(elem) for elem in input()])
set2 = set([int(elem) for elem in input()])

print('NO' if set1.isdisjoint(set2) else 'YES')
