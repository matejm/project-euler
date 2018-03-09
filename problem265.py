

def get_next(start, used):
	l = []

	if start + '1' not in used:
		l.append(start + '1')
	if start + '0' not in used:
		l.append(start + '0')

	return l

def get_arrangements(n, current, used, concat, depth=1):
	if depth == 2 ** n:
		results.append(concat)
		return 1

	for option in get_next(current[1:], used):
		used.add(option)
		get_arrangements(n, option, used, concat + option[-1], depth + 1)
		used.remove(option)


n = 5
start = '0' * n
used = set([start])

results = []
get_arrangements(n, start, used, start)

results = [int(i, 2) >> (n - 1) for i in results]
print(sum(results))