maxim = 100*100

def is_palindromic(n):
	num = str(n)
	for i in range(int(len(num)/2)):
		if num[i] != num[len(num) - i - 1]:
			return False
	return True

for i in range(100, 999):
	for j in range(100, 999):
		if (i * j) > maxim and is_palindromic((i * j)):
			maxim = i * j

print('result: {}'.format(maxim))

assert is_palindromic(4) == True
assert is_palindromic(10) == False
assert is_palindromic(3956593) == True
assert is_palindromic(239652173) == False