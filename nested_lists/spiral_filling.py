arr = [int(elem) for elem in input().split()]
n = arr[0]
m = arr[1]

a = [[0]*arr[1] for i in range(arr[0])]

Ibeg = 0
Ifin = 0
Jbeg = 0
Jfin = 0
    
k = 1
i = 0
j = 0

while (k <= n * m):
    a[i][j] = k;
    if i == Ibeg and j < m - Jfin - 1:
        j += 1
    elif j == m - Jfin - 1 and i < n - Ifin - 1:
        i += 1
    elif i == n - Ifin - 1 and j > Jbeg:
        j -= 1
    else:
        i -= 1

    if (i == Ibeg + 1) and (j == Jbeg) and (Jbeg != m - Jfin - 1):
        Ibeg += 1
        Ifin += 1
        Jbeg += 1
        Jfin += 1
        
    k += 1
    
for i in range(n):
    result = []
    for j in range(m):
            result.append(str(a[i][j]).ljust(3))
    print(*result)
    