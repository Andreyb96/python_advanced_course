n = int(input())
arr = set()

def is_repeat(arr, n):
    for i in range(n + 1):
        s = input()
        length = len(arr)
        arr.add(s)
        if length == len(arr):
            return 'REPEAT'
    return 'OK'

print(is_repeat(arr, n))
    