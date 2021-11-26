functions = []

with open(input()) as file:
    arr = file.readlines()
    for i in range(len(arr)):
        if 'def ' in arr[i]:
            if i == 0:
                functions.append(arr[i].strip().split()[1].split('(')[0])
                continue
            if not arr[i-1].startswith('#'):
                functions.append(arr[i].strip().split()[1].split('(')[0])

if len(functions) > 0:
    for elem in functions:
        print(elem)
else:
    print('Best Programming Team')   
