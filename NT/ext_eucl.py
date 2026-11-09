def ext_eucl(a, b): # O(log min(a, b)) 
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0, y0, a

def find_solutions(a, b, c, ks=range(-2, 3)):
    if a == 0 and b == 0:
        return [(0, 0)] if c == 0 else []
    
    x0, y0, g = ext_eucl(abs(a), abs(b))
    if c % g != 0:
        return []

    x0 *= c // g
    y0 *= c // g
    if a < 0: x0 = -x0
    if b < 0: y0 = -y0

    dx = (b // g) if b != 0 else 0
    dy = (a // g) if a != 0 else 0
    
    return [(x0 + k * dx, y0 - k * dy) for k in ks]

def count_solutions(a, b, c, lx, rx, ly, ry):
    if a == 0 and b == 0:
        return (rx - lx + 1) * (ry - ly + 1) if c == 0 else 0
    if a == 0:
        return rx - lx + 1 if c % b == 0 and ly <= c // b <= ry else 0
    if b == 0:
        return ry - ly + 1 if c % a == 0 and lx <= c // a <= rx else 0

    x0, y0, g = ext_eucl(abs(a), abs(b))
    if c % g != 0:
        return 0

    x0 *= c // g
    y0 *= c // g
    if a < 0: x0 = -x0
    if b < 0: y0 = -y0

    dx, dy = b // g, a // g

    def get_k_range(val0, step, low, high):
        if step > 0:
            return -((low - val0) // -step), (high - val0) // step
        return -((high - val0) // -step), (low - val0) // step

    kx_min, kx_max = get_k_range(x0, dx, lx, rx)
    ky_min, ky_max = get_k_range(y0, -dy, ly, ry)

    k_low = max(kx_min, ky_min)
    k_high = min(kx_max, ky_max)

    return max(0, k_high - k_low + 1)