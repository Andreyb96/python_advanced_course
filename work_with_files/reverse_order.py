with open('data.txt') as file:
    arr = file.readlines()
    for i in range(len(arr)):
        print(arr[len(arr) - 1 - i].strip())
