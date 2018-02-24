from problem51 import primes as generate_primes
from collections import defaultdict
from itertools import combinations

N = 1000000000

primes = generate_primes(int(N**0.5 + 1))

def factor(n):
	factors = defaultdict(int)
	for prime in primes:
		if n == 1: break
		while n % prime == 0:
			factors[prime] += 1
			n //= prime
	return factors

def product(l):
	t = 1
	for i in l: t *= i
	return t

goal = 15499 / 94744

min_res = 1

# pricakuje se, da bo iskano stevilo vsebovalo nizka prastevila
start = 2 * 3 * 5 * 7 * 11 * 13

for d in range(start, N, start):
	factors = factor(d).keys()

	n = 0
	for r in range(1, len(factors) + 1):
		for c in combinations(factors, r):
			n += (-1) ** (r + 1) * d // product(c)

	resilience = d - n

	if resilience / d < min_res:
		min_res = resilience / d
		print(min_res, goal) 

	if resilience / (d - 1) < goal:
		print(d)
		break
