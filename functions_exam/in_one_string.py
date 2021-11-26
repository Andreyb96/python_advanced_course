words = input().split()

sorted_words = sorted(words, key=lambda a: a.lower())

print(*sorted_words)
