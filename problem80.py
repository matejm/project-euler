from decimal import Decimal, getcontext

getcontext().prec = 110

def square_root_sum(n):
	sqrt = Decimal(n).sqrt()

	if sqrt == int(sqrt):
		return 0

	decimals = int(10 ** 99 * sqrt)
	return sum(map(int, str(decimals)))

s = 0
for n in range(2, 101):
	s += square_root_sum(n)

print(s)