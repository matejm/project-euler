from problem51 import primes as generate_primes

n = 1
for i in generate_primes(100):
	if n * i >= 10 ** 6: break
	n *= i

print(n)
 
'''komentar:
Ocitno bo najmanj tujih stevil imelo stevilo, ki bo produkt cim manjsih prastevil.
'''