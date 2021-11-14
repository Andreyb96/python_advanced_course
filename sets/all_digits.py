set1 = set([int(elem) for elem in input()])
set2 = set([int(elem) for elem in input()])

print('YES' if set1.issuperset(set2) else 'NO')
