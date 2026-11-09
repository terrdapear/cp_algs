def build_spf(n):
    spf = [i if i % 2 == 1 else 2 for i in range(n + 1)]
    i = 3
    while i * i <= n:
        if spf[i] == i:
            for j in range(i * i, n + 1, 2 * i):
                if spf[j] == j:
                    spf[j] = i 
        i += 2
    return spf

spf = build_spf(10 ** 5)

def prime_factorize(n): # O(log n)
    f = []
    while n > 1:
        p = spf[n]
        temp = 0
        while spf[n]==p:
            n //= p
            temp += 1
        f.append((p, temp))
    return f
