counter = 0

with open('grades.txt') as file:
    for line in file.readlines():
        arr = [int(elem) for elem in line.strip().split()[1:]]
        if (arr[0] >= 65 and arr[1] >= 65 and arr[2] >= 65):
            counter += 1
        
print(counter)
