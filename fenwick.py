class FenwickTree:
    def __init__(s,arr):
        s.n = len(arr)
        s.T = [0]+list(arr)
        for i in range(1,s.n+1):
            p = i + (i & -i)
            if p<=s.n:
                s.T[p] += s.T[i]

    def sum(s,x): #for diff arrays, sum(x) = a[x]
        x+=1
        total = 0
        while x:
            total+=s.T[x]
            x -= (x & -x)
        return total
   
    def add(s,x,delta): #pt update
        x+=1
        while x<=s.n:
            s.T[x] += delta
            x += (x & -x)

    def query(s,L,R): #inclusive, 0-indexing
        return s.sum(R) - s.sum(L-1)

    def update(s,L,R,delta): #for diff arrays
       s.add(L,delta)
       s.add(R+1,-delta)