from math import sqrt

points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

func = lambda x: sqrt(pow(x[0], 2) + pow(x[1], 2))

print(sorted(points, key=func))
