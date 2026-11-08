from math import isqrt

class SqrtTree:
    def __init__(s, a): #iterable
        s.n = len(a)
        s.B = max(1, isqrt(s.n))
        s.blocks = [a[i:i+s.B] for i in range(0,s.n,s.B)]
        s.sums = [sum(b) for b in s.blocks]     #

    def update(s,x,delta):
        b = x // s.B
        i = x % s.B

        old_val = s.blocks[b][i]
        s.blocks[b][i] = delta
        s.sums[b] += (delta - old_val)          # sum

    def query(s, L, R): #inclusive, 0-indexing
        b1, i1 = L // s.B, L % s.B
        b2, i2 = R // s.B, R % s.B

        if b1 == b2:
            return sum(s.blocks[b1][i1:i2+1])   #

        ans = sum(s.blocks[b1][i1:])            #

        for b in range(b1+1,b2):
            ans += s.sums[b]                    #

        ans += sum(s.blocks[b2][:i2+1])         #
        return ans
