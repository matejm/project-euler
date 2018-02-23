from romans import RomanNumConverter
from roman import toRoman

with open('roman_numerals') as f:
	numerals = f.readlines()

total_len_saved = 0

for num in numerals:
	num = num.rstrip()
	converted_num = toRoman(RomanNumConverter(num).to_integer())
	total_len_saved += len(num) - len(converted_num)

print(total_len_saved)