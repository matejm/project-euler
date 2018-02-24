
def contains_center(A, B, C):
	A, B, C = sorted((A, B, C))

	if A[0] > 0:
		return False

	try:
		k_ab = (B[1] - A[1]) / (B[0] - A[0])
	except ZeroDivisionError:
		# vertical line
		k_ab = (B[1] - A[1]) * 1e19
	try:
		k_ac = (C[1] - A[1]) / (C[0] - A[0])
	except ZeroDivisionError:
		k_ab = (C[1] - A[1]) * 1e19

	k_ao = A[1] / A[0]

	k1, k2 = sorted((k_ab, k_ac))

	if not (k1 <= k_ao and k_ao <= k2):
		return False

	line = line_between_points(B, C)
	if line(A[0]) < A[1] and line(0) < 0:
		return True
	if line(A[0]) > A[1] and line(0) > 0:
		return True

	return False


def line_between_points(A, B):
	x0, y0 = A
	x1, y1 = B
	# I calculated this formula by hand.
	n = (y1 - y0 * x1 / x0) / (1 - x1 / x0)
	k = (y0 - n) / x0

	return lambda x: k * x + n	


with open('triangles') as f:
	triangles = f.readlines()
triangles = [list(map(int, i.split(','))) for i in triangles]

count = 0

for triangle in triangles:
	a1, a2, b1, b2, c1, c2 = triangle
	count += contains_center((a1, a2), (b1, b2), (c1, c2))

print(count)

