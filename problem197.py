from decimal import Decimal, getcontext
from math import floor

getcontext().prec = 20

def f(x):
	a = Decimal(30.403243784)
	x2 = x * x
	r = floor(2 ** (a - x2))
	r = Decimal(r) / Decimal(10 ** 9)
	return r

results = []
results_set = set()

u = Decimal(-1)

while u not in results_set:
	results_set.add(u)
	results.append(u)

	u = f(u)

repeating = results.index(u)

goal = 10 ** 12
goal -= repeating

repeating_results = results[repeating :]


u_n = repeating_results[goal % len(repeating_results)]
u_n1 = repeating_results[(goal + 1) % len(repeating_results)]

print('{:.9f}'.format(u_n + u_n1))
