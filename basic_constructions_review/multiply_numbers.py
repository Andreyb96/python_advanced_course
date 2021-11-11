def findMult(arr):
	for i in range(len(arr)):
		for j in range(len(arr)):
			if (i != j) and arr[i] * arr[j] == num:
				print('ДА')
				return
	print('НЕТ')

n = int(input())
arr = []

for i in range(n):
	arr.append(int(input()))

num = int(input())

findMult(arr)