n = int(input())
result = {}

for i in range(n):
    arr = [elem.strip() for elem in input().split(':')]
    result[arr[0].lower()] = arr[1]
    
m = int(input())

for i in range(m):
    s = input().lower()
    print(result[s] if s in result else 'Не найдено')
