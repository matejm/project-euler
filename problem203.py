
def squarefree(n):
	if n % 4 == 0:
		return False
	i = 3
	while i * i <= n:
		if n % (i * i) == 0:
			return False
		i += 2

	return True

all_coeff = []

l = [1]
for __ in range(51 - 1):
	l2 = [1]
	for i in range(1, len(l)):
		l2.append(l[i - 1] + l[i])
	l2.append(1)

	l = l2
	all_coeff += l

all_coeff = set(all_coeff)

s = 0
for c in all_coeff:
	if squarefree(c):
		s += c

print(s)