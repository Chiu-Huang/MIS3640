def factor (n):
    if n == 0:
        return 1
    return n * factor (n-1)


print (factor (10))




def factorial (n):
    if n == 1:
        return 1
    print ("current n =", n)
    return n * factorial (n-1)

print (factorial(10))