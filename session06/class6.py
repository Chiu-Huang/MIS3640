import turtle 
import time 

def square (s,l):
    for i in range (4):
        s.fd (l) 
        s.right(90)


age = input ("What is your age?")

age = int(age)

if age > 18:
    print("Your age is: {}" .format(age))
    print("adult")
else:
    print("Your age is {}." .format(age))


if age > 18 :
    print ("adult")
elif age >= 6: 
    print ("teenager")
else:
    print ("kid")

def compare (x,y):
    if x == y : 
        print ("x and y are equal")
    else:
        if x < y:
            print ("x is less than y")
        else: 
            print ("x is greater than y")


def countdown(n):
    if n <= 0: 
        print ("Blastoff!")
    else:
        print(n)
        time.sleep(2)
        countdown(n-1)

countdown (3)



def print_n(s,n):
    if n <=0:
        return
    print (s)
    print_n (s,n-1)

print_n ("ijwqewqe",4)

