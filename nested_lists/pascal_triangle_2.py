def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1

def getPascalStr(n):
    result = []
    for i in range(n + 1):
        result.append(int(factorial(n) / (factorial(i) * factorial(n - i))))
    return result

n = int(input())

for i in range(n):
    print(*getPascalStr(i))
    