s = input().lower()

for elem in '.,;:-?!':
    s = s.replace(elem, '')

print(len(set(s.split())))
