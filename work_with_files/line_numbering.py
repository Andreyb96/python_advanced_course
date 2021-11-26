arr = []
counter = 1

with open('input.txt') as file:
    for line in file.readlines():
        arr.append(str(counter) + ') ' + line)
        counter += 1

with open('output.txt', 'w') as file:
    file.writelines(arr)
