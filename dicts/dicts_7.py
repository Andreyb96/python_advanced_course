s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

result = {}

for elem in s.split():
	if elem in result:
		result[elem] += 1
	else:
		result[elem] = 1

n = list(result.values()).count(max(result.values()))


result = dict(sorted(result.items()))

print(list(result.keys())[list(result.values()).index(max(result.values()))])
