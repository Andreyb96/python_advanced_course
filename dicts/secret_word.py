s = input()
n = int(input())
result_1 = {}
result_2 = {}

for i in range(n):
    arr = [elem.strip() for elem in input().split(':')]
    result_2[int(arr[1])] = arr[0]
    
for elem in s:
    if elem in result_1:
        result_1[elem] += 1
    else:
        result_1[elem] = 1

result = ''

for elem in s:
    result += result_2[result_1[elem]]
    
print(result)
