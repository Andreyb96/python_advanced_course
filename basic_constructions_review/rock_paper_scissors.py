def StoneScissorsPaper(first, second):
	if first == 'камень' and second == 'бумага':
		print('Руслан')
	elif first == 'камень' and second == 'ножницы':
		print('Тимур')
	elif first == 'бумага' and second == 'камень':
		print('Тимур')
	elif first == 'бумага' and second == 'ножницы':
		print('Руслан')
	elif first == 'ножницы' and second == 'камень':
		print('Руслан')
	elif first == 'ножницы' and second == 'бумага':
		print('Тимур')

timurChoice = input()
ruslanChoice = input()

if (timurChoice == ruslanChoice):
	print('ничья')

StoneScissorsPaper(timurChoice, ruslanChoice)