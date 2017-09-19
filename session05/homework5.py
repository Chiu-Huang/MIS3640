# python m turtledemo

import math
import turtle

ching = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

def triangle (side)


turtle.speed(9)

turtle.goto(50, 40) 
circle (ching,100)

turtle.setx(30)
turtle.sety(-40)
circle (ching,40)


turtle.mainloop() 



'''polyline(ching,180,4,2)'''
"""turtle.setx(10)
turtle.sety(0)
"""

turtle.setx(0)
turtle.sety(0)









import turtle

turtle.speed(0)

p = turtle.Turtle()

def y (p,r) : 
    p.circle(r,180)
    p.circle(2*r,540)
    p.left(180)
    p.circle(r,180)

y(p,100)
turtle.mainloop() 



