begin = int(input())
end = int(input())

def predicate(num):
    for i in range(len(str(num))):
        if int(str(num)[i]) == 0:
            return False
        if num%int(str(num)[i]) != 0:
            return False
    return True

print(*[i for i in range(begin, end+1) if predicate(i)])
