import random

length = int(input())
result = ""

for i in range(length):
    result += chr(random.randint(65,90))
    
print(result)
