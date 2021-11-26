arr = [elem for elem in input().split()]

func = lambda x: sum([int(elem) for elem in x])

print(*sorted(arr, key=func))
