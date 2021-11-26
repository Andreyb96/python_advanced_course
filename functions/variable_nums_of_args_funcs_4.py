def greet(name, *args):
    result = 'Hello, ' + name + ' and '

    for elem in args:
        result += elem
        result += ' and '

    return result[:-5] + '!'
