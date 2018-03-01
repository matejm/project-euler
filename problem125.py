def is_sum_of_squares(n):
    s = 1 * 1 + 2 * 2

    low = 1
    high = 2

    while low < high:
        if s == n:
            return True
        while s < n:
            high += 1
            s += high * high
        while s > n:
            s -= low * low
            low += 1

    return False

sum_of_palindromes = 0
max_val = 10**8

for i in range(1, 10000):
    si = str(i)
    si_reversed = si[::-1]

    palindrome1 = int(si + si_reversed)
    palindrome2 = int(si + si_reversed[1:])

    if palindrome2 < max_val and is_sum_of_squares(palindrome2):
        sum_of_palindromes += palindrome2
    if palindrome1 < max_val and is_sum_of_squares(palindrome1):
        sum_of_palindromes += palindrome1

print(sum_of_palindromes)
