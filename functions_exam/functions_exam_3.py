words = 'the world is mine take a look what you have started'.split()

print(*map(lambda x: '\"' + x + '\"',words))
