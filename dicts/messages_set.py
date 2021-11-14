d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

s = input().upper()
result = ''

for sym in s:
    for elem in d.items():
        if sym in elem[1]: 
            result += elem[0] * (elem[1].find(sym) + 1)
print(result)
