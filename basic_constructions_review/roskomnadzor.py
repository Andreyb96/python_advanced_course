word = input() + ' запретил букву'

letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

for elem in letters:
	if elem in word:
		print(word + ' ' + elem)
		word = word.replace(elem, "")
		word = word.replace("  ", " ")
		if word.startswith(' '):
			word = word[1:]
		if word.endswith(' '):
			word = word[:-1]
