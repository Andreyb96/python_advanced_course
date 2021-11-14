import random

def generate_ip():
    result = ""
    
    for i in range(4):
        result += str(random.randint(0,255)) + '.'
    
    return result[:-1];
