from functools import reduce

def product_of_odds(data):
    return reduce(lambda a,b: a*b, [elem for elem in data if elem%2==1], 1)
