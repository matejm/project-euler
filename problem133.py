from math import log

def repunit(n, mod):
	if n == 0:
		return 0

	a = 1
	for i in range(int(log(n, 2))):
		b = a // 10
		b *= b
		b %= mod
		b *= 10

		a *= a
		a -= b
		a %= mod

		a *= 10
		a += 1

	m = n - 2 ** int(log(n, 2))
	remaining = repunit(m, mod)
	a *= pow(10, m, mod)

	return (a + remaining) % mod


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

primes = generate_primes(100000)

c = 0
s = 0
for p in primes:
	# never be a factor? Just check first 20 numbers :) It works! 
	for i in range(1, 20):
		if repunit(10 ** i, p) == 0:
			break
	else:
		c += 1
		s += p

	if p % 1000 == 1:
		print(p)

print(s)