text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for elem in text:
	if elem in result:
		result[elem] += 1
	else:
		result[elem] = 1
