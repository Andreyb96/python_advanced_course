def matrix(n=1, m=-1, value=0):
    if m == -1:
        m = n

    arr = []
    for i in range(n):
        arr.append([])
        for j in range(m):
            arr[i].append(value)
    return arr
