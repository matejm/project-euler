
def sum(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

l = []

for base in range(2, 1000):
    for exponent in range(2, 100):
        if sum(base ** exponent) == base:
            l.append(base ** exponent)

l.sort()
print(l[29])