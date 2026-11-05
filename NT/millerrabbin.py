def is_prime(n): #O(k*log^3(n))
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False
    s,d = 0,n-1

    while d%2 == 0:
        d//=2
        s+=1
    bases = [2,3,5,7,11,13,17,19,23,29,31,37]
    for a in bases:
        if n <= a:
            break

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True
