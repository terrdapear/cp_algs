a = []

# Prefix sum arrays and Difference arrays are inverses <3

# _.-._-._.-._.-  Prefix Aggregation  -._-._.-._.-._ #
pref = [0]
for i in range(n):
    pref.append(pref[-1]+a[i])

def query(l,r): # inclusive, 0-indexing
    return pref[r+1]-pref[l]

# _.-._-._.-._.-  Difference Array  -._-._.-._.-._ #
diff = [a[0]]
for i in range(1,n):
    diff.append(a[i]-a[i-1])
# sum(diff[:x+1]) = a[x]

def update(l,r,delta): # inclusive, 0-indexing
    diff[l]+=delta
    diff[r+1]-=delta