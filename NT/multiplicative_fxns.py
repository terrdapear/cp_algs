# These are O( max(log n, time taken to factorize) ) 
# prime_factorize must return [(p,e)]

from math import prod

def tau(n): # number of divisors
    f = prime_factorize(n)
    return prod(e+1 for p,e in f)

def sigma(n): # sum of divisors
    f = prime_factorize(n) 
    return prod((p**(e+1)-1)//(p-1) for p,e in f)

def phi(n): # Euler's totient
    f = prime_factorize(n) 
    return prod((p-1)*p**(e-1) for p,e in f)