with open(input()) as file:
    if len(file.readlines()) < 10:
        file.seek(0)
        for line in file.readlines():
            print(line.strip())
    else:
        file.seek(0)
        for line in file.readlines()[-10:]:
            print(line.strip())
