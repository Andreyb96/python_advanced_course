classNum = int(input())

def isTopScorerInClass(classNum):
    for i in range(classNum):
        pupilsInClass = int(input())
        result = False
        for j in range(pupilsInClass):
            if int(input().split()[1]) == 5:
                result = True
        if not result:
            return False
        result = False
    return True

result = 'YES' if isTopScorerInClass(classNum) else 'NO'
print(result)
