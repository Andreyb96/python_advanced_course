summa = 0

with open('ledger.txt') as file:
    for line in file.readlines():
        summa += int(line.strip()[1:])
        
print('$' + str(summa))
