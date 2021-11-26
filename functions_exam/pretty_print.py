def pretty_print(data, side = '-', delimiter = '|'):
    mainStr = delimiter + ' ' + (' ' + delimiter + ' ').join(map(str, data)) + ' ' + delimiter
    print(' ' + side * (len(mainStr) - 2))
    print (mainStr)
    print(' ' + side * (len(mainStr) - 2))
