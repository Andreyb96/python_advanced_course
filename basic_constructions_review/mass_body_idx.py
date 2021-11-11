mass = float(input())
height = float(input())

bmi = mass / pow(height, 2)

if bmi < 18.5:
	print('Недостаточная масса')
elif bmi <= 25:
	print('Оптимальная масса')
else:
	print('Избыточная масса')