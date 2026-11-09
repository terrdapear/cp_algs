'''
prime_sieve and prime_list was taken from PyRival. Credits to them! 
These functions are highly optimized for PyPy. 
'''

def prime_sieve(n):
    """returns a sieve of primes >= 5 and < n"""
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve


def prime_list(n):
    """returns a list of primes <= n"""
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend([3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1])
    return res


# This simple temp works better for CPython tho
def sieve(n): 
    if n < 2:
        return []
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(4, n + 1, 2):
        prime[i] = False

    p = 3
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, 2 * p):
                prime[i] = False
        p += 2
   
    return [2] + [i for i in range(3, n + 1, 2) if prime[i]]
