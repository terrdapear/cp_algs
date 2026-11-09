from math import gcd
from random import randint

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if is_prime(n):
        return n
    c = randint(1, n - 1)
    f = lambda x: (pow(x, 2, n) + c) % n

    x,y,d = 2,2,1

    while d == 1:
        x = f(x)
    
        y = f(f(y))
        d = gcd(abs(x - y), n)

        if d == n:
            return pollard_rho(n)
       
    return d

def rec(n): #O(n^(1/4))
    if n <= 1:
        return []
    if is_prime(n):
        return [n]
    factor = pollard_rho(n)
    return rec(factor) + rec(n // factor)

from collections import Counter
def prime_factorize(n):
    return [(p, e) for p, e in sorted(Counter(rec(n)).items())]

#simple prime_factorization
from math import isqrt
def prime_factorize(n):
    if n <= 1:
        return []
    if n in [2, 3]:
        return [(n, 1)]

    temp = 0
    while n % 2 == 0:
        n //= 2
        temp += 1
    
    f = [(2, temp)] if temp > 0 else []
    for p in range(3, isqrt(n) + 1, 2):
        temp = 0
        while n % p == 0:
            n //= p
            temp += 1
        if temp > 0:
            f.append((p, temp))
    
    if n > 1:
        f.append((n, 1))
    
    return f