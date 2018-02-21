def primes(n):
	'''Eratostenovo resteto, vrne seznam stevil do vkljucno n, ki so prastevila'''

	l = list(range(n + 1))
	if n > 0: l[1] = 0

	# ucinkoviteje: znebimo se vseh stevil, ki niso poleg veckratnikov stevila 6
	l[4 :: 2] = [0] * ((n - 4) // 2 + 1)
	l[9 :: 3] = [0] * ((n - 9) // 3 + 1)  # python list slicing je **mnogo** hitrejsi, kot ce bi pisali s for loopom
	
	# gledamo samo do korena od n, hitreje
	for i in range(1, (int(n ** 0.5) + 1) // 6 + 1):
		# gremo po veckratnikih stevila 6, pogledamo stevli, ki sta eno manjse in vecje.
		a = 6 * i - 1
		b = 6 * i + 1

		if l[a]:
			l[a*a :: a] = [0] * ((n - a * a) // a + 1)
		if l[b]:
			l[b*b :: b] = [0] * ((n - b * b) // b + 1)

	# vrnemo stevila, ki jih nismo nastavili na 0
	return [i for i in l if i]

def possible_replacement(string_prime):
	'''vrne vse moznosti, kjer lahko zamenjamo znake, razen tiste ko ne zamenjamo nicesar in tiste ko zamenjamo vse'''
	length = len(string_prime)
	return [[bool(i & 2**j) for j in range(length)] for i in range(1, 2 ** length - 1)]

prime_numbers = primes(1000000)
prime_set = set(prime_numbers)

max_count = 0
max_prime = -1
max_replacement = []

if __name__ == '__main__':
	# gremo cez prastevila, za vsako prastevilo naredimo vse mozne zamenjave, in si zapomnimo, kje je najvec zamenjav se vedno prastevil
	for prime in prime_numbers:
		string_prime = str(prime)
		count = 0
		replacement = []
		for replace_indices in possible_replacement(string_prime):
			c = 0
			for i in range(10):
				number = ''.join(i if not replaced else j for i, j, replaced in zip(string_prime, [str(i)] * len(string_prime), replace_indices))
				
				if number[0] == '0':
					continue
				number = int(number)
				
				if number in prime_set:
					c += 1

			if c > count:
				count = c
				replacement = replace_indices

		if count > max_count:
			max_count = count
			max_prime = prime
			max_replacement = replacement
			print(max_prime, max_count, max_replacement)
			if count == 8:
				print(''.join(i if not replaced else j for i, j, replaced in zip(str(max_prime), ['1'] * len(max_replacement), max_replacement)))
				exit()

'''komentar:
Zelo slab pristop, lahko bi delovalo konkretno hitreje, ce bi bolj pozorno prebral navodila. Namesto vseh moznosti bi gledal samo enake stevke pri prastevilih.
Celoten princip je cuden, saj max_prime sploh ni tisto stevilo, ki ga iscemo, ampak mu moramo se zamenjati dolocene stevke v enke.
'''