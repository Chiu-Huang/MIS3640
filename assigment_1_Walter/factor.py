#Q 1
def factor(n):
    i = 2
    list1 = []
    while n > 1:
        if n % i == 0:
            print (i)
            n /= i
            i = 2 
        else:
            i += 1

factor (120)