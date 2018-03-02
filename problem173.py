def bisect_min_hole(outer):
    low = 0
    high = outer - 1

    while low + 1 < high:
        mid = (low + high) // 2

        if outer * outer - mid * mid <= TILES:
            high = mid
        else:
            low = mid

    return high


TILES = 10 ** 6
n = 0

for outer in range(1, TILES):
    min_hole = bisect_min_hole(outer)

    if min_hole >= outer:
        break

    min_hole = max(1, min_hole)

    if outer % 2 != min_hole % 2:
        min_hole += 1

    n += (outer - min_hole) // 2

print(n)
