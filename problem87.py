from bisect import bisect

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

target = 5e7
primes = generate_primes(int(target ** 0.5) + 100)

counter = 0
expressed_numbers = set()

for p1 in primes:
	p1 = p1 ** 4
	if p1 >= target: break
	
	for p2 in primes:
		p2 = p2 ** 3
		if p1 + p2 >= target: break

		for p3 in primes:
			p3 = p3 ** 2
			if p1 + p2 + p3 >= target: break

			if p1 + p2 + p3 in expressed_numbers:
				continue

			counter += 1
			expressed_numbers.add(p1 + p2 + p3)

print(counter)