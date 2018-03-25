from decimal import Decimal, getcontext

getcontext().prec = 20

digits = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

A = Decimal((1 + 5 ** 0.5) / 2)
sqrt5 = Decimal(5 ** 0.5)

def pow(a, n):
	r = Decimal(1)

	while n:
		if n & 1:
			r *= a
		n >>= 1
		a *= a

		a /= Decimal(10 ** a.adjusted())
		r /= Decimal(10 ** r.adjusted())

	return r

def is_pandigital(n):
	s = set()
	while n > 0:
		s.add(n % 10)
		n //= 10

	return s == digits

def start_pandigital(n):
	a = pow(A, n)

	num = int((a / sqrt5) * 10 ** 9)
	while num > 10 ** 9:
		num //= 10
	return is_pandigital(num)

a = 1
b = 1

for i in range(3, 10 ** 6):
	a, b = a + b, a
	a %= 10 ** 9
	b %= 10 ** 9

	if is_pandigital(a % 10 ** 9):
		if start_pandigital(i):
			print(i)
			break
