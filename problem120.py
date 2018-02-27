def get_r_max(a_squared):
    r = -1
    k1, k2 = 1, 1    

    for n in range(a_squared):
        r1 = (k1 + k2) % a_squared
        r = max(r, r1)
    
        k1 *= (a - 1)
        k1 %= a_squared
        k2 *= (a + 1)
        k2 %= a_squared
    return r

s = 0

for a in range(3, 1000 + 1):
    s += get_r_max(a * a)
    
    if a % 10 == 0:
        print(a)

print(s)