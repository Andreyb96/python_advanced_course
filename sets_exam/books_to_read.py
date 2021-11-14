m = int(input())
n = int(input())
library = []
toRead = []

for i in range(m):
    library.append(input())
    
for i in range(n):
    toRead.append(input())
    
for elem in toRead:
    if elem in library:
        print('YES')
    else:
        print('NO')
        