import re

def FindAnton(name, num):
	if re.match(r'[\w\W]*a[\w\W]*n[\w\W]*t[\w\W]*o[\w\W]*n[\w\W]*', name):
		return str(num)
	return ''

n = int(input())
s = ''

for i in range(n):
	fridgeName = input()
	s += FindAnton(fridgeName, i + 1)
    
print(' '.join(s))