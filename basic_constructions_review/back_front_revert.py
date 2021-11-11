def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

s = input()

l = s.split()

for i in range(len(l)//2):
	l = swapPositions(l, i*2, i*2 + 1)

print(*l)