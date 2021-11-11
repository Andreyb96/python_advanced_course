s = input()
result = ''

for i in range(len(s)):
	result += s[::-1][i]
	if i%3==2 and i+1 != len(s):
		result += ','

print(result[::-1])