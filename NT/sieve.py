def sieve(n): #O(n log log n)
    if n<2:
        return []
    prime = [True]*(n+1)
    prime[0] = prime[1] = False

    for i in range(4,n+1,2):
        prime[i]=False

    p = 3
    while p*p<=n:
        if prime[p]:
            for i in range(p*p,n+1,2*p):
                prime[i]=False
        p+=2
   
    return [2]+[i for i in range(3,n+1,2) if prime[i]]
