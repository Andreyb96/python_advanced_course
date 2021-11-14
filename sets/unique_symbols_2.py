n = int(input())
word = ''

for i in range(n):
    word += input().lower()
print(len(set(word)))
