def isInSphere(arr1, arr2, arr3):
    for i in range(len(arr1)):
        if sum([pow(elem, 2) for elem in [arr1[i], arr2[i], arr3[i]]]) > 4:
            return False
    return True

abscissas = [float(elem) for elem in input().split()]
ordinates = [float(elem) for elem in input().split()]
applicates = [float(elem) for elem in input().split()]

print(isInSphere(abscissas, ordinates, applicates))
