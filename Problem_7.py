target = 10001

start = 500001
prims = [True] * start
prims[0] = False
prims[1] = False
primes = []

while len(primes) < target:
	prims.extend([True] * 250000)
	for i in range(2, (start - 1)):
		if prims[i] == True:
			primes.append(i)
			for j in range(i, (start - 1), i):
				prims[j] = False

print('result: {}'.format(primes[target - 1]))