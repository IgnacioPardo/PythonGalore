def add_ellip(p, A, P, Q): # points are in format (x, y)
	z = 0 # representing special 0 point

	if (P == z):
		return Q
	if (Q == z):
		return P

	if P[0] == Q[0]:
		if (P == (Q[0], -Q[1] % p)):
			return z
		else:
			m = ((3*pow(P[0], 2, p) + A)*pow(2*P[1], p-2, p)) % p
	else:
		m = (P[1] - Q[1])*pow(P[0] - Q[0], p-2, p) % p

	x = (pow(m, 2, p) - P[0] - Q[0]) % p
	y = (m*(P[0] - x) - P[1]) % p
	return (x, y)

def pow2floor(x):
	p = 1
	x >>= 1
	while (x > 0):
		x >>= 1
		p <<= 1
	return p

def multi_nP(p, A, n, P):
	d = {}

	def rec_helper(n, P):
		if (n == 0):
			return (0, 0)
		elif (n == 1):
			return P
		elif (n in d):
			return d[n]
		else:
			p2f = pow2floor(n)
			remainder = n - p2f

			lower_half = rec_helper(p2f//2, P)
			d[p2f//2] = lower_half
			nP = add_ellip(p, A, lower_half, lower_half)

			if (remainder):
				nP = add_ellip(p, A, nP, rec_helper(remainder, P))

			d[n] = nP
			return nP

	return rec_helper(n, P)

from icecream import ic
from random import randint

def bits(n):
	return len(bin(n)[2:])

def f(x):
	return [float((x**3+A*x**2+x)**(1/2)), -float((x**3+A*x**2+x)**(1/2))][0]

def keys(G):
	priv = randint(0, r)
	public = multi_nP(p, A, priv, (G, int(f(G))))
	return priv, public

def secret(minePriv, otherPublic):
	return multi_nP(p, A, minePriv, otherPublic)[0]

def baseKey(r):
	#random Point on Curve25519
	#x ∈ ℤ, y ∈ ℤ

	x = randint(1, r)
	while not (y := f(x)).is_integer():
		ic(x, y)
		x = randint(1, r)
	y = int(y)
	return x


def is_prime(num, test_count):
	if num == 1:
		return False
	if test_count >= num:
		test_count = num - 1
	for x in range(test_count):
		val = randint(1, num - 1)
		if pow(val, num-1, num) != 1:
			return False
	return True

def generate_big_prime(n):
	found_prime = False
	while not found_prime:
		p = randint(2**(n-1), 2**n)
		if is_prime(p, 1000):
			return p

r = 115792089237316195423570985008687907853269984665640564039457584007913129639935

#p, A: D-H values
p = generate_big_prime(128)
A = 486662

G = baseKey(r)

#bob
bobPriv, bobPublic = keys(G)

#alice
alicePriv, alicePublic = keys(G)

#bob
secretKey = secret(bobPriv, alicePublic)

#alice
secretKey_ = secret(alicePriv, bobPublic)


import warnings
if not secretKey == secretKey_:
	CRED = '\033[91m'
	CEND = '\033[0m'
	print(CRED + "WRONG" + CEND)
ic(p, G, f(G), bobPriv, bits(bobPriv), bobPublic, bits(bobPublic[0]), alicePriv, bits(alicePriv), alicePublic, bits(alicePublic[0]), secretKey, bits(secretKey))