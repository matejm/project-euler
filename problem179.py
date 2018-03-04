from collections import defaultdict
from copy import copy

def generate_primes(n):
    l = list(range(n + 1))
    if n > 0: l[1] = 0

    l[4 :: 2] = [0] * ((n - 4) // 2 + 1)
    l[9 :: 3] = [0] * ((n - 9) // 3 + 1)
    
    for i in range(1, (int(n ** 0.5) + 1) // 6 + 1):
        a = 6 * i - 1
        b = 6 * i + 1

        if l[a]:
            l[a*a :: a] = [0] * ((n - a * a) // a + 1)
        if l[b]:
            l[b*b :: b] = [0] * ((n - b * b) // b + 1)

    return [i for i in l if i]

def factor(n):
    f = -1
    for prime in primes:
        if n == 1 or prime * prime > n:
            break
        if n % prime == 0:
            f = prime
            n //= prime
            break

    if f == -1:
        d = defaultdict(int)
        d[n] = 1
        return d

    lower_factors = copy(factors[n])
    if lower_factors is None:
        d = defaultdict(int)
        d[f] = 1
        return d
    
    lower_factors[f] += 1
    return lower_factors

def divisors(n):
    d = 1
    for f in factors[n]:
        d *= factors[n][f] + 1
    return d


primes = generate_primes(int((10**7) ** 0.5) + 1)

factors = [None for i in range(10**7)]

factors[1] = defaultdict(int)

last = 1
c = 0


for i in range(2, 10**7):
    factors[i] = factor(i)

    div = divisors(i)
    if last == div:
        c += 1

    last = div

    if i % 10000 == 0:
        print(i)

print(c)