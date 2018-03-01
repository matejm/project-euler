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


def rad(n):
    factors = []
    for prime in primes:
        if n == 1:
            break
        if n % prime == 0:
            factors.append(prime)
            n //= prime
        while n % prime == 0:
            n //= prime
    
    r = 1
    for f in factors:
        r *= f
    return r

primes = generate_primes(100001)

numbers = [i for i in range(1, 100001)]

numbers.sort(key=lambda x : (rad(x), x))

print(numbers[10000 - 1])