def gcd (x,y):
    if x % y == 0:
        return y
    elif y % x ==0:
        return x       
    elif x > y:
        return gcd (y, x % y)
    elif x < y:
        return gcd (x, y % x)
    


def gcd (x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x % y)
