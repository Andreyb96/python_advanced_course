colours = dict()
totalAmount = 0
readColoursOn = False
readGoatsOn = False
result = []

with open('goats.txt') as file:
    for line in file.readlines():
        if line == 'COLOURS\n':
            readColoursOn = True
            continue
        if line == 'GOATS\n':
            readColoursOn = False
            readGoatsOn = True
            continue

        if readColoursOn:
            colours[line.strip()] = 0
        if readGoatsOn:
            colours[line.strip()] += 1
            totalAmount += 1

for (key, value)in colours.items():
    if value/totalAmount > 0.07:
        result.append(key + '\n')

with open('answer.txt', 'w') as file:
    file.writelines(sorted(result))
