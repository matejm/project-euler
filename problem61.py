from copy import copy

def check(start, possible, begin):
	global s

	if not possible:
		if begin == start:
			return True
		return False

	for n in possible:
		for i in range(11, 100):
			if 100 * start + i in P[n]:
				new_possible = copy(possible)
				new_possible.remove(n)
				if check(i, new_possible, begin):
					s += 100 * start + i
					print(100 * start + i)
					return True

	return False


P = [[], [], []] + [[0] * 10 ** 5 for i in range(3, 8 + 1)]

for i in range(1, 10 ** 5):
	P[3][i] = i * (i + 1) // 2
	P[4][i] = i * i
	P[5][i] = i * (3 * i - 1) // 2
	P[6][i] = i * (2 * i - 1)
	P[7][i] = i * (5 * i - 3) // 2
	P[8][i] = i * (3 * i - 2)

for i in range(1, 9):
	P[i] = set(P[i])

s = 0
for i in range(11, 100):
	if check(i, set([3, 4, 5, 6, 7, 8]), i):
		break

print(s)
