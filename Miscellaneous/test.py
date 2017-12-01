def diff21(n):
    if n > 21:
        return 2 * (n - 21)
    else:
        return 21 - n

def double(n):
    return 2*n

print(diff21(21))
print(double(diff21(30)))
