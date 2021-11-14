m = int(input())
n = int(input())

maths = set()

for i in range(m + n):
    maths.add(input())

if len(maths) - (n + m - len(maths)) == 0:
    print('NO')
else:
    print(len(maths) - (n + m - len(maths)))
    