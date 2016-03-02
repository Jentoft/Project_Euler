goal = 20

#The result will be the product of the largest exponents of all the primes less than the goal that are less than the goal
# example: for 10, the result is 2520 = 8 * 9 * 5 * 7 = 2^3 * 3^2 * 5^1 * 7^1

def primes_lte(n):
	ps = [True] * (n + 1)
	ps[0] = False
	ps[1] = False
	results = []

	for i in range((n + 1)):
		if ps[i]:
			for j in range(2* i, (n + 1), i):
				ps[j] = False

	for i in range((n + 1)):
		if ps[i]:
			results.append(i)

	return results

def largest_prime_exponents(n):
	results = []
	for i in primes_lte(n):
		temp = i
		while (temp * i) <= n:
			temp *= i
		results.append(temp)
	return results

product = 1
for i in largest_prime_exponents(goal):
	product *= i

print('The result is: {}'.format(product))

assert primes_lte(2) == [2], primes_lte(2)
assert primes_lte(10) == [2, 3, 5, 7]

assert largest_prime_exponents(10) == [8, 9, 5, 7], largest_prime_exponents(10)