def fib (n):
    if n > 2:
        return fib (n-1) + fib(n-2)
    elif n == 2 or n == 1:
        return 1 
