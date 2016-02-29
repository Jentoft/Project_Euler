num_1 = 1
num_2 = 2
iterator = 0
total = 0

while num_2 <= 4000000:
	if (iterator % 3) == 0: #every third fibbonaci number is even
		total += num_2
	temp = num_2 + num_1
	num_1 = num_2
	num_2 = temp
	iterator += 1

print('Result: {}'.format(total))