def sqrt(x):
    for i in range(1, x):
        if i**2 == x:
            return i
        elif i ** 2 > x:
            return i - 1
        else:
            continue

print(sqrt(5))


def binary_search(x):
    l, r = 0, x
    res = 0
    
    while l <= r:
        m = (l+r)//2
        if m**2 > x:
            r = m-1
        elif m**2<x:
            l = m+1
            res = m
        else:
            return m
        
    return res
"""
    m = x/2
    res = 0
    if m**2 > x:
        m-1
    elif m**2 < x:
        res = m
        m + 1  
    else:
        m
"""

print(binary_search(10))