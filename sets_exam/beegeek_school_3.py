m = int(input())
n = int(input())

maths = set()
informatics = set()

for i in range(m):
    maths.add(input())
    
for i in range(n):
    informatics.add(input())

if len(maths.symmetric_difference(informatics)) == 0:
    print('NO')
else:
    print(len(maths.symmetric_difference(informatics)))
    