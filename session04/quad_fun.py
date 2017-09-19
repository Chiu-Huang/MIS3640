#Exercise 1

def f2 (a,b,c): 
    root1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    root2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    print (root1)
    print ("The possible values for x is: ", root1 , "or", root2)



#Session05 review

def give_me_a_break():
    str1 = "break"
                      # return is an ending pt of a function
    print ("another break")
    return str1


def f1 (x):
    if isinstance (x, int) or isinstance (x,float):    # dont need  == True
        if x >= 0:
            return x 
        else: 
            return -x
    else:
        print ("error,please type a number")



    else:
        print ("error, please type a number")

print (give_me_a_break())
