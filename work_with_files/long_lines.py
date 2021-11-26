max_len = 0
max_str = []

with open('lines.txt') as file:
    for line in file.readlines():
        if len(line) > max_len:
            max_len = len(line)
            max_str = [line]
        elif len(line) == max_len:
            max_str.append(line)
            
for elem in max_str:
    print(elem, end = '')
