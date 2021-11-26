from random import randint

with open('random.txt', 'w') as file:
    arr = [str(randint(111, 777)) + '\n' for i in range(25)]
    file.writelines(arr)
