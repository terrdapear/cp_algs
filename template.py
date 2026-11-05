import sys
#sys.setrecursionlimit(300_000)

def solve():
    input_dat = sys.stdin.read().split()

    it = iter(input_dat)
    out = []
    
    I = lambda : int(next(it)) 
    S = lambda : next(it) 
    O = out.append
    
    t = I()
    for _ in range(t):
        pass#ans
        
    print("\n".join(map(str,out)))

solve()