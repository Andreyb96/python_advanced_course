position = [sym for sym in input()]

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
position[0] = d[position[0]]
position[1] = int(position[1])

for i in range(8):
    arr = []
    for j in range(8):
        if j == position[0] - 1 and i == 8 - position[1]:
	        arr.append('N')
        elif position[0]-2 > 0 and j == position[0] - 3 and (i == 8 - position[1] + 1 or i == 8 - position[1] - 1):
            arr.append('*')
        elif position[0]+2 < 9 and j == position[0] + 1 and (i == 8 - position[1] + 1 or i == 8 - position[1] - 1):
            arr.append('*')
        elif position[1] - 2 > 0 and i == 8-position[1]+2 and (j == position[0] - 2 or j == position[0]):
            arr.append('*')
        elif position[1] + 2 < 9 and i == 8-position[1]-2 and (j == position[0] - 2 or j == position[0]):
            arr.append('*')
        else:
            arr.append('.')
    print(*arr)
    