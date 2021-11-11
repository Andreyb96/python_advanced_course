n = int(input())
k = int(input())

people = [i for i in range(1, n+1)]
popIdx = 0

while (len(people) > 1):
	popIdx = (popIdx + k) % len(people)-1 if (popIdx + k) % len(people)-1 != -1 else len(people) - 1;
	people.pop(popIdx)

print(people[0])