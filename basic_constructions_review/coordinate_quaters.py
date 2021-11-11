numDots = int(input())

dotsQuarters = {"Первая четверть" : 0, "Вторая четверть" : 0, "Третья четверть" : 0, "Четвертая четверть" : 0}

for i in range(numDots):
	[x,y] = input().split()
	x = int(x)
	y = int(y)
	if x > 0 and y > 0:
		dotsQuarters["Первая четверть"] += 1
	elif x < 0 and y > 0:
		dotsQuarters["Вторая четверть"] += 1
	elif x < 0 and y < 0:
		dotsQuarters["Третья четверть"] += 1
	elif x > 0 and y < 0:
		dotsQuarters["Четвертая четверть"] += 1

for key, value in dotsQuarters.items():
	print(key + ": " + str(value))