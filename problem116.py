from collections import defaultdict

memo = defaultdict(int)

def calculate(tile, place):
    if tile > place:
        return 1

    if memo[(tile, place)]:
        return memo[(tile, place)]

    place_tile = calculate(tile, place - tile)
    skip_square = calculate(tile, place - 1)

    r = place_tile + skip_square
    memo[(tile, place)] = r
    return r

red_tile = calculate(2, 50) - 1
green_tile = calculate(3, 50) - 1
blue_tile = calculate(4, 50) - 1

print(red_tile + green_tile + blue_tile)