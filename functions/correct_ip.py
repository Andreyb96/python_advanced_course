def isIPAddressCorrect(address):
    for elem in address.split('.'):
        if not elem.isdigit():
            return False
        if int(elem) < 0 or int(elem) > 255:
            return False
    return True

print(isIPAddressCorrect(input()))
