file = open('nums.txt')
summa = 0

for line in file.read().split():
    summa += int(line)

print(summa)
file.close()
