from collections import defaultdict

memo = defaultdict(int)

def calculate(tile, place):
    if tile > place:
        return 1
    if memo[place]:
        return memo[place]

    skip_square = calculate(tile, place - 1)
    place_tile = 0

    for i in range(place - tile + 1):
        place_tile += calculate(tile, i - 1)

    r = skip_square + place_tile
    memo[place] = r
    return r

for n in range(50, 1000):
    c = calculate(50, n)

    if c > 10**6:
        print(n)
        break