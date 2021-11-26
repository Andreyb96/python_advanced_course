password = input()

def predicate(password):
    if len(password) < 7:
        return False
    result = [False, False, False]
    for sym in password:
        if sym.islower():
            result[0] = True
        if sym.isdigit():
            result[1] = True
        if sym.isupper():
            result[2] = True
    return all(result)
       
print('YES' if predicate(password) else 'NO')
