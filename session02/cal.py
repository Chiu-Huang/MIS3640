#Exercise 1
r = 5
pi = 3.14
Volume = 4/3*pi*r**3
print("the Volume of a sphere with radius 5 is {:.2f}." .format (Volume))


c = 24.95
n = 60
cost = c + 3 + 0.75 * (n-1)
print("$",cost)

Rseconds = 15 *2 + 12 * 3
Rminutes = 52 + 8 + 3 * 7 + 8
Rhours = 6

seconds = Rseconds % 60
minutes = (Rminutes + round (Rseconds/60)) % 60
hours = round ((Rminutes + round (Rseconds/60))/60) + Rhours   # need adjustment on the round, should be rounddown

print (hours,":",minutes,":",seconds)


    grade = (89-82)/82 *100
    print ("percentage increase is {:04.1f}%.".format(grade))   # 04 represents 4 spaces, dots included, 04 "0" means that there will be a 0 in the front