s = input()
value = len(s) * 0.6

print(str(int(value)) + ' р. ' + str(round(value%1*100)) + ' коп.')