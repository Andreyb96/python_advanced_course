def sq_sum(*args):
    summa = 0
    for elem in args:
        summa += pow(float(elem), 2)
    if (summa%1 == 0):
        summa = int(summa)
    return summa
