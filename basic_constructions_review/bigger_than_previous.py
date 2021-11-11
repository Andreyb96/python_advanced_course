s = input()
counter = 0

for i in range(len(s.split()) - 1):
	if int(s.split()[i]) < int(s.split()[i + 1]):
		counter += 1

print(counter)