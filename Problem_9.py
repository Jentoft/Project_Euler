target = 1000
result = []

for a in range(1, (target - 1)):
	for c in range(a, target):
		b = target - a - c
		if b <= 0:
			continue
		temp = sorted([a, b, c])
		if ((temp[0] **2) + (temp[1] ** 2)) == (temp[2] ** 2):
			result = temp
			break
	if result != []:
		break

if len(result) != 3:
	print('Please, please, dont happen')
else:
	print('The answer is: {}'.format((result[0] * result[1] * result[2])))