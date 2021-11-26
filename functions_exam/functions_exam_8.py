def arithmetic_operation(operation):
    if operation == '+':
        return lambda a,b: a + b
    if operation == '-':
        return lambda a,b: a - b
    if operation == '*':
        return lambda a,b: a * b
    if operation == '/':
        return lambda a,b: a / b
