target = 2000000

nums = [True] * target #2 milion is even, therefore not a prime, therefore I can ignore it
nums[0] = False
nums[1] = False
primes = []

for i in range(2, target):
	if nums[i] == True:
		primes.append(i)
		for j in range(i, target, i):
			nums[j] = False

print('answer: {}'.format(sum(primes)))