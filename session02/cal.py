r = 5
pi = 3.14
Volume = 4/3*pi*r**3
print(Volume)


c = 24.95
n = 60
cost = c + 3 + 0.75 * (n-1)
print("$",cost)

Rseconds = 15 *2 + 12 * 3
Rminutes = 52 + 8 + 3 * 7 + 8
Rhours = 6

seconds = Rseconds % 60
minutes = (Rminutes + round (Rseconds/60)) % 60
hours = round ((Rminutes + round (Rseconds/60))/60) + Rhours

print (hours,":",minutes,":",seconds)


grade = (89-82)/82 *100
print ("percentage increase is %.1f %%" %grade) 