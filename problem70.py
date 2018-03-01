from collections import defaultdict
from copy import copy

def generate_primes(n):
    l = list(range(n + 1))
    if n > 0: l[1] = 0

    l[4 :: 2] = [0] * ((n - 4) // 2 + 1)
    l[9 :: 3] = [0] * ((n - 9) // 3 + 1)
    
    for i in range(1, (int(n ** 0.5) + 1) // 6 + 1):
        a = 6 * i - 1
        b = 6 * i + 1

        if l[a]:
            l[a*a :: a] = [0] * ((n - a * a) // a + 1)
        if l[b]:
            l[b*b :: b] = [0] * ((n - b * b) // b + 1)

    return [i for i in l if i]

def factor(n):
	original = n
	f = -1
	for p in primes:
		if p * p > n or n == 1:
			break

		if n % p == 0:
			f = p
			n //= f
			break

	if f == -1:
		if n != 1:
			d = defaultdict(int)
			d[n] = 1

			factors[n] = d
			return

	d = copy(factors[n])
	d[f] += 1

	factors[original] = d

def phi(n):
	r = n
	for p in factors[n]:
		r //= p
		r *= p - 1
	return r

def sum_of_digits(n):
	s = 0
	while n:
		s += (n % 10)
		n //= 10
	return s 

primes = generate_primes(int((10 ** 7) ** 0.5))
print('Primes generated')

factors = [None for i in range(10 ** 7)]
factors[1] = defaultdict(int)

for i in range(2, 10 ** 7):
	factor(i)
	if i % 10 ** 5 == 0: print(i)

print('Factorized')

min_ratio = 100
n = -1

for i in range(2, 10 ** 7):
	p = phi(i)
	if sum_of_digits(p) == sum_of_digits(i) and sorted(str(i)) == sorted(str(p)):
		if i / p < min_ratio:
			min_ratio = i / p
			n = i
	if i % 10 ** 5 == 0: print(i)

print(n) 
