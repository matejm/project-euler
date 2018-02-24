from collections import defaultdict

LENGTH = 100

memo = [[-1] * 10 for i in range(101)]

def number_of_options(index, final_index, digit):
	'''returns number of possible increasing numbers with `final_index` number of digits.
	Dynamic programming'''
	if memo[index][digit] != -1:
		return memo[index][digit]

	if index == final_index:
		return 1

	options = 0
	# Calculate possible options, increase digit or not...
	for new_digit in range(digit, 10):
		options += number_of_options(index + 1, final_index, new_digit)

	memo[index][digit] = options
	return options

increasing = number_of_options(0, LENGTH, 0)
memo = [[-1] * 10 for i in range(101)]  # clear memo

decreasing = 0
for i in range(1, LENGTH + 1):
	decreasing += number_of_options(0, i, 0)
	decreasing -= 10  # constant numbers, both increasing and decreasing
	memo = [[-1] * 10 for i in range(101)]  # clear memo


total = increasing + decreasing
total -= 1  # 0 is not included

print(total)