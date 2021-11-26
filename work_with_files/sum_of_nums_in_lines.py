with open('numbers.txt') as file:
    for line in file.readlines():
        print(sum([int(elem) for elem in line.split()]))
