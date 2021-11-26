numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

minimum = 1000
maximum = -1

minimum_arr = tuple()
maxiumum_arr = tuple()

for elem in numbers:
    if sum(elem) / len(elem) > maximum:
        maxiumum_arr = elem
        maximum = sum(elem) / len(elem)
    if sum(elem) / len(elem) < minimum:
        minimum_arr = elem
        minimum = sum(elem) / len(elem)

print(minimum_arr)
print(maxiumum_arr)
