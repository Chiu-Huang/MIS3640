#Exercise 1

def f2 (a,b,c): 
    root1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    root2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    print (root1)
    print ("The possible values for x is: ", root1 , "or", root2)






def print_twice (name):
    print (name)
    print (name)




def cat_twice (part1, part2):
    cat = part1 + part2
    print_twice (cat)



def gmab ():
    str1 = 'break'
    return str1
print (gmab())

def gmab():
    str1 = 'break'

def area_of_circle (x):
    print(3.14 * x ** 2)

area_of_circle (10)


type (42)


type ('42')
int ('42')       # turning into int, can be float -> int
str (3.13)
abs (-100)
max (1,2)    # https://docs.python.org/3/library/functions.html#type

round (3.12314,2)
ord ("c")    # = chr () ^ -1    
chr ("_")

import math
dir (math)

ratio = 100
math.log10(ratio)

degrees = 45 
radians = degrees/ 180.0 * math.pi # math.pi is not a function. It is a constant
math.sin (radians)


def my_abs (x) :
    print (abs (x))



def x ():
    pass  # pass makes statement skip

abs ('A')


def my_abs (x) :
    if isinstance (x) == int or float:
    print ("failure, please type a number") 
            else print (abs (x))

def f1 (x):
    if isinstance (x, int) or isinstance (x,float) == True:
        print (abs (x))
    else:
        print ("error, please type a number")


import math
def move (x,y, step, angle):
    nx = x + step * math.cos (angle)
    ny = y + step * math.sin (angle)
    return nx,ny

x,y = move (100,100,60,math.pi /6)
print (x,y)