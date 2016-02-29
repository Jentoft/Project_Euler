import math

target = 600851475143
array_size = 5 * (10 ** 8)

def prime_numbers_lte(n):
	print("next block")
	primes = []
	for i in range(math.ceil(n/array_size)):
		if i == 0:
			starting = 2
		else:
			starting = i * array_size
		prim_subset = [True] * array_size
		#If n is before the end of the array, only search up to n
		if (starting + array_size) > n:
			ending = n + 1
		else:
			if i == 0:
				ending = array_size - 1
			else:
				ending = starting + array_size
		for j in primes: #Setting all multiples of currently known primes to False
			#To guarantee I don't try to access a number before prim_subset, I start at the first
			#multiple of the prime after the start of prim_subset.  If the start is a multiple of j
			#...I guarantee prim_subset[0] is False
			prim_subset[0] = (((starting % j) != 0) and prim_subset[0])
			for k in range((starting + j - (starting % j)), ending, j):
				prim_subset[k - starting] = False
		for j in range(starting, ending):
			if i == 0:
				beginning = 0
			else:
				beginning = starting
			if prim_subset[j - beginning] == False:
				continue
			primes.append(j)
			#I only need to worrry about multiples within the same prim_subset for the first block
			if i == 0: 
				for k in range(j, ending, j):
					prim_subset[k] = False
	return primes

# def prime_numbers_lte(n):
# 	if n < 2: return []
# 	if n == 2: return [2]
# 	primes = [3] #actual list of primes to return
# 	prime_multiples = [6] #list of the multiples of primes with corresponding index in primes
# 	for i in range (3, int(n) + 1, 2):
# 		print(str(i))
# 		#if i exceeds any of the prime multiples, update said multiples
# 		while i > min(prime_multiples):
# 			min_index = prime_multiples.index(min(prime_multiples))
# 			prime_multiples[min_index] += primes[min_index]
# 		if i in prime_multiples: #if the number is in prime_multiples, it's composite
# 			continue
# 		else: #otherwise it's prime, so update all three lists
# 			primes.append(i)
# 			prime_multiples.append(i * 2)
# 	return primes

def largest_factor(n, candidates):
	for num in reversed(candidates):
		if (n % num) == 0:
			return num
	raise ValueError('none of {} divides into {}'.format(candidates,n))

prims = prime_numbers_lte(target)

assert largest_factor(20, range(1,20)) == 10
assert largest_factor(20, range(1,21)) == 20

assert prime_numbers_lte(2) == [2], prime_numbers_lte(2)
assert prime_numbers_lte(10) == [2, 3, 5, 7], prime_numbers_lte(10)
assert prime_numbers_lte(20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert prime_numbers_lte(0) == []
assert prime_numbers_lte(1) == []