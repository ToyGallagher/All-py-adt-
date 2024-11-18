def recurged(a,b):
    low = min(a,b)
    high = max(a,b)
    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return recurged(low,high%low)
print(recurged(6, 39))