countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'New York', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for elem in list(zip(countries, capitals, population)):
    print(elem[1] + ' is the capital of ' + elem[0] + ', population equal ' + str(elem[2]) + ' people.')
