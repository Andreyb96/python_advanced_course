import re

with open('forbidden_words.txt') as file:
    forbidden_words = file.read().strip().split()

with open(input()) as file:
    for line in file.readlines():
        for elem in forbidden_words:
            if elem in line.strip().lower():
                insensitive_hippo = re.compile(re.escape(elem), re.IGNORECASE)
                line = insensitive_hippo.sub('*'*len(elem), line).strip()
        print(line.strip())
