from fractions import Fraction

all_fractions = set()

low = 1 / 3
high = 1 / 2

all_fractions = []

print('Generating fractions')
for d in range(2, 12000 + 1):
	for n in range(d // 3, min(d // 2 + 2, d)):
		f = n / d
		if low < f and f < high:
			all_fractions.append(Fraction(n, d))
	if d % 100 == 0:
		print(d)

print('Counting unique fractions')

unique_fractions = set(all_fractions)
print(len(unique_fractions))
