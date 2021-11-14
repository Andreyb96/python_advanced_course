def build_query_string(params):
    result = ''
    for elem in sorted(params):
        result += elem
        result += '='
        result += str(params[elem])
        result += '&'
    return result[:-1]
    