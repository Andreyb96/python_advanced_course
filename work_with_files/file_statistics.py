linesNum = 0
wordsNum = 0
lettersNum = 0

with open('file.txt') as file:
    for line in file.readlines():
        linesNum += 1
        wordsNum += len(line.split())
        lettersNum += len([elem for elem in line if elem.isalpha()])

print("Input file contains:\n" + str(lettersNum) + " letters\n" + str(wordsNum) + " words\n" + str(linesNum) + " lines")
