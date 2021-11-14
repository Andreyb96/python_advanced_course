import random

def generate_password(length):
    result = []
    digits = '23456789';
    small_letters = 'qwertyuipasdfghjkzxcvbnm';
    huge_letters = 'QWERTYUPASDFGHJKLZXCVBNM';
    s = "qwertyuipasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVBNM23456789"
    result += random.sample([elem for elem in digits], 1)
    result += random.sample([elem for elem in small_letters], 1)
    result += random.sample([elem for elem in huge_letters], 1)
    result += random.sample([elem for elem in s], length - 3)
    print(''.join(result))

def generate_passwords(count, length):
    for i in range(count):
        generate_password(length)

n, m = int(input()), int(input())

generate_passwords(n, m)
