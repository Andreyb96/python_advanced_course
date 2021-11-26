def mean(*args):
    summa  = 0.0
    counter = 0
    for elem in args:
        if type(elem) == type(0) or type(elem) == type(0.0):
            summa += elem
            counter += 1
    if counter == 0:
        return summa
    return summa / counter
