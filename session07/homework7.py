def sqroot (a):
    x = 5
    y = 5
    error = 0.0005
    while True:
        x = y
        y = (x+ a/x)/2
        if abs (y * y - a) < error:
            break
    print ("{:.03f}".format (y))




def mysqrt (a):
    x = a/2
    y = x
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return (x)

import math 
def test_square_root(n):
    L = []
    for i in range(1, n + 1, 1):
        L += [float(i), mysqrt(i), math.sqrt(i), abs(mysqrt(i) - math.sqrt(i))]
    L = ["a", "mysqrt(a)", "math.sqrt(a)", "diff"] + L
    L = [L[x:x+4] for x in range(0, len(L), 4)]
    for row in L:
        print ("{: >4} {: >24} {: >24} {: >24}".format(*row))

test_square_root(10)



# def test_square_root (n):
#     print ("a   mysqrt(a)     math.sqrt(a)  diff")
#     print ("---------------------------------------")
#     for i in range (1,n+1,1):
#         print (float(i)) and mysqrt(i) and math.sqrt(i) and abs(mysqrt(i)-math.sqrt(i))

# def t (n):
#     print ("a   mysqrt(a)     math.sqrt(a)  diff")
#     print ("---------------------------------------")
#     for i in range (1,n+1,1):
#         print (float(i),mysqrt(i),math.sqrt(i),abs(mysqrt(i)-math.sqrt(i)))
        



# def help_list4(L):
#     if len (L) % 4 = 0:
#         for e          




#     print ()
#     print ("---------------------------------------")
#     for i in range (1,n+1,1):
#         print (float(i),mysqrt(i),math.sqrt(i),abs(mysqrt(i)-math.sqrt(i)))

