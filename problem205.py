pyramidal = [0] * 37
pyramidal[0] = 1

for dice in range(9):
    pyramidal_new = [0] * 37

    for current_sum in range(0, 37):
        if pyramidal[current_sum] == 0: continue

        for side in range(4):
            pyramidal_new[current_sum + side + 1] += pyramidal[current_sum]

    pyramidal = pyramidal_new

cubic = [0] * 37
cubic[0] = 1

for dice in range(6):
    cubic_new = [0] * 37

    for current_sum in range(0, 37):
        if cubic[current_sum] == 0: continue

        for side in range(6):
            cubic_new[current_sum + side + 1] += cubic[current_sum]

    cubic = cubic_new


cubic_sum = [0] * 37
for i in range(1, 37):
    cubic_sum[i] = cubic_sum[i - 1] + cubic[i]

cubic_total = cubic_sum[-1]
pyramidal_total = sum(pyramidal)

win_sum = 0

for possible_result in range(37):
    if possible_result == 0: continue

    win = cubic_sum[possible_result - 1] / cubic_total
    win *= pyramidal[possible_result] / pyramidal_total

    win_sum += win

print('{:.7f}'.format(win_sum))