arr = []

with open('class_scores.txt') as file:
    for line in file.readlines():
        arr.append(line.strip().split()[0] + ' ' + str(int(line.strip().split()[1]) + 5 if int(line.strip().split()[1]) < 95 else 100) + '\n')

with open('new_scores.txt', 'w') as file:
    file.writelines(arr)
