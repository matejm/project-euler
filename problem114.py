from collections import defaultdict

memo = defaultdict(int)

tile = 3

def calculate(place):
    if tile > place:
        return 1
    if memo[place]:
        return memo[place]

    skip_square = calculate(place - 1)
    place_tile = 0

    for i in range(place - tile + 1):
        place_tile += calculate(i - 1)

    r = skip_square + place_tile
    memo[place] = r
    return r

print(calculate(50))