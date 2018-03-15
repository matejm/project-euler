def hamming_numbers(n, i=0):
	if i >= len(primes):
		return 0
	if n == 1:
		return 1


	number_of_combinations = 0
	for j, p in enumerate(primes):
		if i > j:
			continue
		if n >= p:
			c = hamming_numbers(n // p, i=j)
			number_of_combinations += c

	return number_of_combinations + 1


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97][:: -1]

print(hamming_numbers(10 ** 9))