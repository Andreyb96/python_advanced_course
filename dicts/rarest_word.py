arr = [elem.strip('.,!?:;-').lower() for elem in input().split()]
result = {}

for elem in arr:
    if elem in result:
        result[elem] += 1
    else:
        result[elem] = 1
        
result = dict(sorted(result.items()))

print(list(result.keys())[list(result.values()).index(min(result.values()))])
