numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {}

for elem in numbers:
    result[elem] = []
    for i in range(1, elem + 1):
        if elem%i == 0:
            result[elem].append(i)
