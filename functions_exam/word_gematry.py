n = int(input())
words = []

def calculate_gematry(word):
    summa = 0
    word = word.upper()
    for elem in word:
        summa += ord(elem) - ord('A')
    return summa

for i in range(n):
    words.append(input())

sorted_words = sorted(words)  
sorted_words = sorted(sorted_words, key=calculate_gematry)    

for elem in sorted_words:
    print(elem)
