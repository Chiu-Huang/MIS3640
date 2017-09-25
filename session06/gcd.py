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

import turtle
import math

g = turtle.Turtle()

def polyline (g,n,l,angle):
    g.speed(0)
    for i in range (n):
        g.fd(l)
        g.lt(angle)

def circle (g,r):
    g.speed(0)
    arc (g,r,360)    

def arc (g,r,angle):
    g.speed(0)
    polyline (g,int(720*angle/360),2*math.pi*r/720,360/720)

turtle.mainloop()