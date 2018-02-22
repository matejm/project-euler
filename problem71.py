from fractions import Fraction

numerator = None
min_error = 1

for d in range(1, 10**6):
	# bisekcija
	low = 1
	high = d

	while low + 1 < high:
		mid = (low + high) // 2
		
		if mid / d < 3 / 7:
			low = mid
		else:
			high = mid
	n = low

	error =  3 / 7 - n / d
	if error < min_error and error > 0:
		min_error = error
		numerator = n

print(numerator)