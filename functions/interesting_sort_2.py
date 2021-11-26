arr = [int(elem) for elem in input().split()]
arr = sorted(arr)
func = lambda x: sum([int(elem) for elem in str(x)])

print(*sorted(arr, key=func))
