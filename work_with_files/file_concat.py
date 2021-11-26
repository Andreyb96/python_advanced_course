n = int(input())
result = ''

for i in range(n):
    with open(input()) as file:
        result += file.read()
    
with open('output.txt', 'w') as file:
    file.write(result)
