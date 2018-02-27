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

primes = generate_primes(10**6)
m = -1
for i, p in enumerate(primes):
    n = i + 1
    
    a = pow(p - 1, n, p * p)
    b = pow(p + 1, n, p * p)

    result = (a + b) % (p * p)

    if result > 10**10:
        print(n)
        break