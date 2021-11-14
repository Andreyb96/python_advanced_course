import random

def generate_password(length):
    s = "qwertyuipasdfghjkzxcvbnmQWERTYUPASDFGHJKLZXCVBNM23456789"
    print(''.join(random.sample([elem for elem in s], length)))

def generate_passwords(count, length):
    for i in range(count):
        generate_password(length)

n, m = int(input()), int(input())

generate_passwords(n, m)
