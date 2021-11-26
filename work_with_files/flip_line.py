with open('text.txt') as file:
    line = file.read()
    print(line[::-1])
