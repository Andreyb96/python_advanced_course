def evaluate(coefficients, x):
    summa = 0
    for i in range(len(coefficients)):
        summa += coefficients[i] * pow(x, len(coefficients) - i - 1)
        
    return summa

coefficients = [int(elem) for elem in input().split()]
x = int(input())

print(evaluate(coefficients, x))
