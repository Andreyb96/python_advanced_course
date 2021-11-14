def merge(values):
    result = {}
    for elem in values:
        for i in elem:
            if i in result:
                result[i].add(elem[i])
            else:
                result[i] = set()
                result[i].add(elem[i])

    return result
    