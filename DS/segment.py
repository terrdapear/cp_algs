class SegmentTree:
    def __init__(s,a):
        s.a = [x for x in a]
        while len(s.a).bit_count()!=1:
            s.a.append(0)                      #

        s.n = len(s.a)
        s.T = [0]*(2*s.n+1)                    #

        for i in range(s.n):
            s.T[s.n+i]=s.a[i]
        for i in range(s.n-1,0,-1):
            s.T[i]= s.T[2*i] + s.T[2*i+1]      # sum
        
    def f(s,node,node_l,node_r,l,r):
        if l<=node_l and node_r<=r:
            return s.T[node]
        if node_r<l or r<node_l:
            return 0                           #
        last_left = (node_l+node_r)//2         #vv
        return s.f(2*node,node_l,last_left,l,r) + s.f(2*node+1,last_left+1,node_r,l,r)

    def query(s,l,r): #inclusive, zero-indexing
        return s.f(1,0,s.n-1,l,r)

    def update(s,x,delta):
        i = s.n+x
        s.T[i]+=delta                          #
        while i>1:
            i//=2
            s.T[i]+=delta                      #

    def assign(s,x,y):
        i = s.n+x
        s.T[i]=y
        while i>1:
            i//=2
            s.T[i]=s.T[2*i]+s.T[2*i+1]         #

