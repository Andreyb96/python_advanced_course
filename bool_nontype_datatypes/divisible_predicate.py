# объявление функции
def func(num1, num2):
    if num1 % num2 == 0:
        return True
    return False

# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print('делится')
else:
    print('не делится')