def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if is_prime(n):
        return n
    c = random.randint(1, n - 1)
    f = lambda x: (pow(x, 2, n) + c) % n

    x,y,d = 2,2,1

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)

        if d == n:
            return pollard_rho(n)
       
    return d

def prime_factorize(n): #O(n^(1/4))
    if n <= 1:
        return []
    if is_prime(n):
        return [n]
    factor = pollard_rho(n)
    return primeFactorize(factor) + primeFactorize(n // factor)
