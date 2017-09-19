import turtle

turtle.speed(0)

a = turtle.Turtle()
c = turtle.Turtle()
p = turtle.Turtle()

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def tri (t,l):
    polyline (t,3,l,120)
def com (p,r) : 
    p.speed(0)
    p.circle(r,360)
    p.circle(r,-30)
    p.left(30)
    tri(p,r)
    p.right(30)
    p.circle(r,90)
    p.left(30)
    tri(p,r)
    p.right(30)
    p.circle(r,90)
    p.left(30)
    tri(p,r)
    p.right(30)
    p.circle(r,90)
    p.left(30)
    tri(p,r)
    p.fd(0.5*r)
    ir = r / (2 * 3 **0.5)
    p.circle(ir,360)
    p.fd(0.5*r)
    p.left(30)
    p.circle(r,30)
    p.left(30)
    p.fd(0.5*r)
    ir = r / (2 * 3 **0.5)
    p.circle(ir,360)
    p.fd(0.5*r)
    p.left(30)
    p.circle(r,30)
    p.left(30)
    p.fd(0.5*r)
    ir = r / (2 * 3 **0.5)
    p.circle(ir,360)
    p.fd(0.5*r)
    p.left(30)
    p.circle(r,30)
    p.left(30)
    p.fd(0.5*r)
    ir = r / (2 * 3 **0.5)
    p.circle(ir,360)
    p.fd(0.5*r)
    p.left(30)
    p.circle(r,30)
    p.left(30)
    



com(a,100)






def sp (p,r) :
    p.speed(0)
    p.circle(r,360)
    p.left (60)
    p.circle(r,120)
    p.up()
    p.home()
    p.left(120)
    p.down()
    p.circle(-r,120)
    p.up()
    p.home()
    p.circle(r,180)
    p.down()
    p.left (120)
    p.circle(-r,120)
    p.up()
    p.home()
    p.circle(r,180)
    p.down()
    p.left(60)
    p.circle(r,120)
    p.left(60)
    p.up()
    p.circle(r,60)
    p.down()
    p.left(120)
    p.circle(-r,120)
    p.left(120)
    p.up()
    p.circle(r,60)
    p.down()
    p.left(120)
    p.circle(-r,120)
 

sp (c,100)


def y (p,r) : 
    p.speed(0)
    p.circle(r,180)
    p.circle(2*r,540)
    p.left(180)
    p.circle(-r,180)
    p.up()
    p.left(90)
    p.fd(r)
    p.down()
    p.circle(r/4,360)
    p.right(180)
    p.up()
    p.fd(2*r)
    p.down()
    p.circle(r/4,360)

y(p,100)
turtle.mainloop() 


