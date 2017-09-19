import turtle

alex = turtle.Turtle ()

print(alex)
alex.fd (100)
alex.lt (90)
alex.fd (100)
alex.lt (90)
alex.fd (100)
alex.lt (90)
alex.fd (100)

turtle.mainloop()


#_________________________________________________________



def square (t):
    print (t)
    for i in range (4):
        t.fd (100)
        t.lt (90)


peter = turtle.Turtle ()

square (peter)

turtle.mainloop ()



def square (t, length,angle,frequency):
    print (t)
    for i in range (frequency):
        t.fd (length)
        t.lt (angle)


peter = turtle.Turtle ()

square (peter, 30,30,12)

turtle.mainloop ()


peter = turtle.Turtle ()

def polygon (shape,side,length):
    print (shape)
    for i in range (side):
        shape.fd (length)
        shape.lt (360/side)

polygon (peter,50,45)

turtle.mainloop ()










for i in range (4):
    print ("hello!")