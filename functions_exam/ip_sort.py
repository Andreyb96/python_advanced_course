n = int(input())
ip_addresses = []

def calculate_digit(ip):
    arr = [int(elem) for elem in ip.split('.')]
    return arr[0]*pow(256, 3) + arr[1]*pow(256, 2) + arr[2]*pow(256, 1) + arr[3]*pow(256, 0) 

for i in range(n):
    ip_addresses.append(input())
    
ip_addresses = sorted(ip_addresses, key = calculate_digit)
for elem in ip_addresses:
    print(elem)
