from math import sqrt


def next(blue, total):
	blue = 3 * blue + 2 * total - 2
	total = int(sqrt(2 * blue * (blue - 1))) + 1

	return blue, total

def check(blue, total):
	return 2 * blue * (blue - 1) == total * (total - 1)

blue = 15
total = 21

while total < 10 ** 12:
	blue, total = next(blue, total)

print(blue)