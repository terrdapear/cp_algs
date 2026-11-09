# These are O( max(log n, time taken to factorize) ) 
# prime_factorize must return [(p,e)]

from math import prod

def tau(n): # number of divisors
    f = prime_factorize(n)
    d = 1
    for p, e in f:
        d *= e + 1
    return d

def sigma(n): # sum of divisors
    f = prime_factorize(n) 
    s = 1
    for p, e in f:
        s *= (p ** (e + 1) - 1)//(p - 1)
    return s

def phi(n): # Euler's totient
    f = prime_factorize(n) 
    t = 1
    for p, e in f:
        t *= (p - 1) * p ** (e - 1)
    return t