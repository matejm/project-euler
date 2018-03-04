import sys
sys.setrecursionlimit(2000)

def pow_pow(a, b, m):
    if b == 1:
        return a
    return pow(a, pow_pow(a, b - 1, m), m)

print(pow_pow(1777, 1855, 10 ** 8))