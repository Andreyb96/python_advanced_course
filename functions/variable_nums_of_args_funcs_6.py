def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(key + ": " + str(value))
