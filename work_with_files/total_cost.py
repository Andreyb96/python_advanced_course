file = open('prices.txt')
summa = 0

for line in file.readlines():
    arr = line.split()
    summa += int(arr[1]) * int(arr[2])

print(summa)
file.close()
