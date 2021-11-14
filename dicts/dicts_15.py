words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {}

for elem in words:
    result[elem] = []
    for i in elem:
        result[elem].append(ord(i))
