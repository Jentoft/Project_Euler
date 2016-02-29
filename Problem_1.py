end = 1000
numOne = 3
numTwo = 5
total = 0

total = sum(range(0, end, numOne)) + sum(range(0, end, numTwo)) - sum(range(0, end, (numOne * numTwo)))
# for i in range(end):
# 	if(i % numTwo) == 0 or (i % numOne) == 0:
# 		total += i

print('The total is: {}'.format(total))
