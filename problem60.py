from problem51 import primes
from itertools import combinations

def check_all_concats(l):
	'''Preveri vze mozne zdruzitve nizov, vrne True ce so vsa prastevila, drugace False'''
	for a, b in combinations(l, 2):
		a, b = str(a), str(b)
		if not (int(a + b) in primes_set and int(b + a) in primes_set):
			return False 
	return True

prime_numbers = primes(100000000)
primes_set = set(prime_numbers)
p = prime_numbers[:1100]
del prime_numbers

n = len(p)

min_sum = 1e9

for i1 in range(n):
	print(i1, n, p[-1])
	for i2 in range(i1, n):
		if not check_all_concats((p[i1], p[i2])):
			continue
		for i3 in range(i2, n):
			if not check_all_concats((p[i1], p[i2], p[i3])):
				continue
			for i4 in range(i3, n):
				if not check_all_concats((p[i1], p[i2], p[i3], p[i4])):
					continue
				for i5 in range(i4, n):
					if not check_all_concats((p[i1], p[i2], p[i3], p[i4], p[i5])):
						continue

					min_sum = min(sum((p[i1], p[i2], p[i3], p[i4], p[i5])), min_sum)

print(min_sum)

'''komentar:
sigurno obstaja lepsi nacin. kako se to naredi, verjetno tudi ne bi bilo treba generirati
prastevil do 10**8, vendar je mi je bilo laje uporabiti funkcijo, ki sem jo ze napisal
za problem 51.
'''