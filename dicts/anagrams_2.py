word_1 = {}
word_2 = {}

for word in [elem.strip('.,!?:;-') for elem in input().lower().split()]:
    for elem in word:
        if elem in word_1:
            word_1[elem] += 1
        else:
            word_1[elem] = 1

for word in [elem.strip('.,!?:;-') for elem in input().lower().split()]:
    for elem in word:
        if elem in word_2:
            word_2[elem] += 1
        else:
            word_2[elem] = 1
               
print('YES' if word_1 == word_2 else 'NO')
