goal = 100
squares = 0
total = 0

for i in range((goal + 1)):
	squares += i ** 2
	total += i

print('squares: {}.  total: {}'.format(squares, total))

print('result: {}'.format((total ** 2) - squares))