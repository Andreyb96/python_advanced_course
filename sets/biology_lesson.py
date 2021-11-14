set1 = set([int(elem) for elem in input().split()])
set2 = set([int(elem) for elem in input().split()])
set3 = set([int(elem) for elem in input().split()])
superSet = {0,1,2,3,4,5,6,7,8,9,10}

print(*sorted(superSet - set1 - set2 - set3))
