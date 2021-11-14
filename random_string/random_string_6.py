import random

def generate_index():
    result = ''
    
    result += chr(random.randint(65, 90))
    result += chr(random.randint(65, 90))
    result += str(random.randint(0, 99))
    result += '_'
    result += str(random.randint(0, 99))
    result += chr(random.randint(65, 90))
    result += chr(random.randint(65, 90))
    
    return result
