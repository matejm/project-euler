from math import log

with open('base_exp') as f:
	data = f.readlines()

data = [list(map(int, i.split(','))) for i in data]

# Idea: a^b = e^(b * log a)
# calculate b * log a and find larges value

values = [log(i) * j for i, j in data]

print(values.index(max(values)) + 1)