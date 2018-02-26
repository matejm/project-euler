from itertools import permutations

def generate_primes(n):
    ''' Sieve of Eratosthenes, for more information see problem 51. '''
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

def check_prime(p):
    for prime in primes:
        if p % prime == 0:
            return False
        if prime ** 2 > p:
            break
    return True

def generate_sets(start, left):
    if not left:
        start.sort()
        all_sets.append(tuple(start))

    p = 0
    for i, digit in enumerate(left):
        p = 10 * p + digit
        if p in primes_set or p > 10**7 and check_prime(p):
            generate_sets(start + [p], left[i + 1:])


primes = generate_primes(10**7)
primes_set = set(primes)
all_sets = []

k = 0
for i in permutations(range(1, 10)):
    generate_sets([], i)
    if k != i[0]:
        print(k)
        k = i[0]

all_sets = set(all_sets)
print(len(all_sets))
