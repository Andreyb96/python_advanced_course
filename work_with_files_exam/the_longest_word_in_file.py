with open('words.txt') as file:
    line = file.read().strip().split()

for elem in list(filter(lambda x: len(x) == len(sorted(line, key = lambda x: len(x), reverse=True)[0]), line)):
    print(elem)
