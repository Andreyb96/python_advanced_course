from random import randint

with open('population.txt') as file:
    for line in file.readlines():
        if (line.startswith('G') and int(line.strip().split()[-1]) > 500000):
            print(line.strip().split()[0])
