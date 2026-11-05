def ext_eucl(a,b): # O(log n) returns x, y, g 
    if (b==0): # ax + by = g
        return 1,0,a
    x1,y1,g = ext_eucl(b,a%b)
    x = y1
    y = x1 - y1*(a//b)
    return x,y,g

def find_solutions(a,b,c,ks=range(-2, 3)):
    x0,y0,g = extgcd(a,b)
    
    if c % g != 0:
        return []  # no sol
    
    x_base = x0 * (c // g)
    y_base = y0 * (c // g)
    
    step_x = b // g
    step_y = a // g
    
    solutions = []
    for k in ks:
        x = x_base + k * step_x
        y = y_base - k * step_y
        solutions.append((x, y))
        
    return solutions

import math

def count_solutions(a, b, c, min_x, max_x, min_y, max_y):
    x0, y0, g = extgcd(a, b)
    
    if c % g != 0:
        return 0
    
    x0 *= c // g
    y0 *= c // g
    
    dx,dy = b//g , a//g
    
    def get_k_bounds(val0, step, low_b, high_b):
        k1 = (low_b - val0) / step
        k2 = (high_b - val0) / step
        return (min(k1, k2), max(k1, k2))

    kx_min, kx_max = get_k_bounds(x0, dx, min_x, max_x)
    ky_min, ky_max = get_k_bounds(y0, -dy, min_y, max_y)
    
    k_low = math.ceil(max(kx_min, ky_min))
    k_high = math.floor(min(kx_max, ky_max))
    
    return max(0, k_high - k_low + 1)