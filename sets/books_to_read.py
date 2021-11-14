n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())
t = int(input())
a = int(input())

onlyOneBook = 2*(x + y + z) - 3*(n+m+k) + 3*t
twoBooks = 2*(n+m+k) - x - y - z - 3*t
noBooks = a + n + m + k - x - y - z - t

print(onlyOneBook)
print(twoBooks)
print(noBooks)
