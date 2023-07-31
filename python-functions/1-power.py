def pow(a, b):
    value = 1
    
    if b < 0:
        a = 1 / a
        b = abs(b)
        
    for _ in range(b):
        value *= a
        
    return value(value, 2)