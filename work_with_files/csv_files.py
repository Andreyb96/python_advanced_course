def read_csv():
    needWriteKeys = True
    keys = []
    result = []

    with open('data.csv') as file:
        for line in file.readlines():
            if needWriteKeys:
                keys = line.strip().split(',')
                needWriteKeys = False
            else:        
                result.append(dict(zip(keys, line.strip().split(','))))
    return result
