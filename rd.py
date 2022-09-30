min = int(input())
max = int(input())

counter = 0
while min != max + 1:
	if min % 2 == 0:
		print(min)
	min += 1
	counter += 1
	if counter > 999:
		break