class SegmentTree:
    def __init__(s, a):
        s.n = 1
        while s.n < len(a):
            s.n <<= 1
        s.T = [0]*(2 * s.n + 1)                 # identity value

        for i in range(len(a)):
            s.T[s.n + i] = a[i]
        for i in range(s.n-1, 0, -1):
            s.T[i] = s.T[2 * i] + s.T[2 * i + 1]# sum
        
    def f(s, node, nl, nr, l, r):
        if l <= nl and nr <= r:
            return s.T[node]
        if nr < l or r < nl:
            return 0                            #

        mid = (nl + nr) >> 1
        left = 2 * node
        right = left + 1

        res = 0                                 #
        if l <= mid:
            res += s.f(left, nl, mid, l, r)     #
        if r > mid:
            res += s.f(right, mid+1, nr, l, r)  #
        return res
        
    def query(s, l, r): #inclusive, 0-indexing
        return s.f(1, 0, s.n-1, l, r)

    def add(s, x, delta):
        i = s.n + x
        s.T[i] += delta                         #
        while i > 1:
            i //= 2
            s.T[i] += delta                     #

    def assign(s, x, y):
        i = s.n + x
        s.T[i] = y
        while i > 1:
            i //= 2
            s.T[i] = s.T[2 * i] + s.T[2 * i +1] #