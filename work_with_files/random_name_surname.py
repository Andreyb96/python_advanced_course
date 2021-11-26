from random import randint

firstNames = []
lastNames = []

with open('first_names.txt') as file:
    for line in file.readlines():
        firstNames.append(line)

with open('last_names.txt') as file:
    for line in file.readlines():
        lastNames.append(line)

for i in range(3):
    print(firstNames[randint(0, len(firstNames))].strip() + ' ' + lastNames[randint(0, len(lastNames))].strip())
