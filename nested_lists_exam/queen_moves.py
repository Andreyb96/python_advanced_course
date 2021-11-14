slovarx = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
slovary = {'8':0, '7':1, '6':2, '5':3, '4':4, '3':5, '2':6, '1':7, '0':8}

position = input()
arr = []

for i in range(8):
    arr.append([])
    for j in range(8):
        if j == slovarx[position[0]] and i == slovary[position[1]]:
            arr[i].append('Q')
        elif j == slovarx[position[0]] or i == slovary[position[1]]:
            arr[i].append('*')
        elif abs(slovarx[position[0]] - j) == abs(slovary[position[1]] - i):
            arr[i].append('*')
        else:
            arr[i].append('.')
        
for i in range(8):
    print(*arr[i])
    