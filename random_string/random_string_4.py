import random

result = set()

while len(result) < 7:
    result.add(random.randint(1,49))
    
print(*sorted(result))
