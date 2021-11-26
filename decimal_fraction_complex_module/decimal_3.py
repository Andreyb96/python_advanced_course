from decimal import *
num = Decimal(input())

arr = sorted([int(elem) for elem in str(num) if elem.isdigit()])
             
print(arr[0] + arr[-1])
