from collections import defaultdict

memo = defaultdict(int)

red_tile = 2
green_tile = 3
blue_tile = 4

def calculate(place):
    if red_tile > place:
        return 1
    if memo[place]:
        return memo[place]

    place_red = calculate(place - red_tile)
    place_green, place_blue = 0, 0

    if green_tile <= place:
        place_green = calculate(place - green_tile)
    if blue_tile <= place:
        place_blue = calculate(place - blue_tile)

    skip_square = calculate(place - 1)

    r = place_red + place_green + place_blue + skip_square
    memo[place] = r
    return r


print(calculate(50))