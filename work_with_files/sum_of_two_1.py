file = open('numbers.txt')
summa = 0

for line in file.readlines():
    summa += int(line)

print(summa)
file.close()
