# These are O(log n) iff prime factorization is O(log n)
# prime_factorize must return { p:e }

def tau(n): # number of divisors
    primes = prime_factorize(n)
    d = 1
    for p,e in primes.items():
        d*=e+1
    return d

def sigma(n): # sum of divisors
    primes = prime_factorize(n) 
    s = 1
    for p,e in primes.items():
        s*= (p**(e+1)-1)//(p-1)
    return s

def phi(n): # Euler's totient
    primes = prime_factorize(n) 
    f = 1
    for p,e in primes.items():
        f*=(p-1) * p**(e-1)
    return f




