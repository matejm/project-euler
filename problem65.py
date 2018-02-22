from fractions import Fraction

def next_value(i):
	if i % 3 == 2:
		t = 2 * (i // 3 + 1)
	elif i == 0:
		t = 2
	else:
		t = 1

	if i < 99:
		return Fraction(t) + Fraction(1, next_value(i + 1))
	return t

fraction = next_value(0)
print(fraction)

digits_in_numerator = map(int, str(fraction.numerator))
print(sum(digits_in_numerator))