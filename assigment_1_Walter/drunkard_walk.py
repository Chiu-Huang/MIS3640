# Q3 and Q4 Combined

import math
import random
import turtle
pi = math.pi
def drunkard_walk(x, y, n):
    """
    x, y: the original location
    n: the number of intersections(steps)
    return the distance after n intersections(steps) from the origin, each block is 100 pixel by default
    """
    movex = 0
    movey = 0
    k = turtle.Turtle()
    k.speed(0)
    k.up()
    k.goto(x*100, y*100)
    #set position (x,y)
    k.down()
    for i in range (0,n,1):
        angle = random.choice ([0,90,180,270])
        #represents 4 directions 
        rad = angle * pi/180
        # sin and cos takes radian instead of angle
        movex += round (math.sin (rad),1)
        movey += round (math.cos (rad),1)
        k.left (angle)
        # determine which direction to go
        k.fd (100)
        #distance 100 pixel per block
        k.right (angle)
        # reverse back to the original angle
    print("The drunkard started from (%d,%d)." % (x, y))
    distance = round ((movex**2 + movey**2)**0.5,2)
    # show distances assuming that we can go through the walls, if not the distance formula will be different
    print("After", n, "intersections, he's", distance, "blocks from where he started.")    
    turtle.mainloop()




p = random.randint(-5,5)
t = random.randint(0,30)
drunkard_walk(p,p,t)

