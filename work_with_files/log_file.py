import io

result = []

with io.open('logfile.txt', encoding='utf-8') as file:
    for line in file:
        name = line.strip().split(', ')[0]
        startTime = line.strip().split(', ')[1]
        endTime = line.strip().split(', ')[2]
        if int(endTime.split(':')[0]) - int(startTime.split(':')[0]) > 1:
            result.append(name + '\n')
        if int(endTime.split(':')[0]) - int(startTime.split(':')[0]) == 1 and int(endTime.split(':')[1]) - int(startTime.split(':')[1]) >= 0:
            result.append(name + '\n')

with open('output.txt', 'w') as file:
    file.writelines(result)
