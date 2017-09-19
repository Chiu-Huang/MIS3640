import turtle
jerry = turtle.Turtle ()
print (jerry)
turtle.mainloop()

# keyword arguments    (n=8, length = 100.0, alex)


import math
import turtle

alex  = turtle.Turtle ()
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle (t,r):
    circumference = 2 * math.pi * r 
    n = 50
    length = circumference / n 
    polygon (t,n,length)

circle (alex,80)

turtle.mainloop()


def poly (t,n,length) :
    angle = 360 / r
    for i in range((n * angle/360)//1):
        t.fd(length)
        t.lt(angle)
    
def arc (t,r,angle):
    r = radius
    t = shape 
    angle = portion

    circumference = 2 * math.pi * r 
    n = 100
    length = circumference / n 
     (t,n,length)

    
    
    
    



def polyline (t,n,l,a,arc):
    for i in range (n):
        t.fd (l)
        t.lt (a)
    """     Hello, this is a failed equation """





