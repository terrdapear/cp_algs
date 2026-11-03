def SUM(T, x):  # in a difference array, SUM(x) = a[x]
    x += 1
    total = 0
    while x:
        total += T[x]
        x -= x & -x
    return total

def ADD(T, x, delta):
    x += 1
    n = len(T)
    while x < n:
        T[x] += delta
        x += x & -x

def QUERY(T, L, R):  # inclusive, 0-indexing
    return SUM(T, R) - SUM(T, L - 1)

def build_fenwick(a):
    n = len(a)
    T = [0] + list(a)
    for i in range(1, n + 1):
        p = i + (i & -i)
        if p <= n:
            T[p] += T[i]
    return T

def RANGE_UPDATE(T, L, R, delta):  # for difference arrays
    ADD(T, L, delta)
    ADD(T, R + 1, -delta)