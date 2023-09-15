def pow(a, b):
    # Check for special cases
    if b == 0:
        return 1
    elif b < 0:
        return 1 / pow(a, -b)

    result = 1
    for _ in range(b):
        value *= a

    return value
