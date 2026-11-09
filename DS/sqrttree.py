from math import isqrt

class SqrtTree:
    def __init__(s, a): 
        s.a = list(a)
        s.n = len(s.a)
        s.B = max(1, isqrt(s.n))
        
        s.sums = [0] * ((s.n + s.B - 1) // s.B)
        for i in range(s.n):
            s.sums[i // s.B] += s.a[i]                  # sum

    def assign(s, x, y):
        b = x // s.B
        old = s.a[x]
        s.a[x] = y
        s.sums[b] += (y - old)                          # invertible only

    def add(s, x, delta): 
        s.a[x] += delta
        s.sums[x // s.B] += delta                       # 

    def query(s, L, R): 
        b1, b2 = L // s.B, R // s.B
        ans = 0                                         # identity value

        if b1 == b2:
            for i in range(L, R + 1):
                ans += s.a[i]                           # 
            return ans

        for i in range(L, (b1 + 1) * s.B):
            ans += s.a[i]                               # 
        for b in range(b1 + 1, b2):
            ans += s.sums[b]                            # 
        for i in range(b2 * s.B, R + 1):
            ans += s.a[i]                               # 

        return ans