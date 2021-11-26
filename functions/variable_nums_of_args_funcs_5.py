def print_products(*args):
    counter = 1
    result = str(counter) + ') '

    for elem in args:
        if type(elem) is str and len(elem) != 0:
            result += elem
            counter += 1
            result += '\n' + str(counter) + ') '    

    if counter == 1:
        print('Нет продуктов')
        return

    print(result[:-4])
