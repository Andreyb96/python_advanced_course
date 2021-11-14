coords = [int(input()) for i in range(3)]

result = ( -1 * coords[1]/(2 * coords[0]), (4 * coords[0] * coords[2] - pow(coords[1],2)) / (4 * coords[0]))

print(result)
