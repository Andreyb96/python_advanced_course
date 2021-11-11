s = input()

counter = 0
maxCounter = 0

for elem in s:
	if elem == 'О':
		if (counter > maxCounter):
			maxCounter = counter
		counter = 0
	else:
		counter += 1;

print(maxCounter if maxCounter > counter else counter)