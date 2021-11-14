m = int(input())
n = int(input())

maths = set()
informatics = set()

for i in range(m):
    maths.add(input())
    
for i in range(n):
    informatics.add(input())
    
print(len(maths.difference(informatics)))
