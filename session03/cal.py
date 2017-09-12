n = 100 # statement, which contains expression n and 100


print (3.14e-2)  # scientific notion works in python
print (1.5 * 4)  # float * int works in python 
print (2**1000)  
len (str(2**10000)) # str --> convert number to string, len --> count length


import math 
print (math.pi)
print (math.sqrt(85))

import random
print (random.random())
random.choice ([1,2,3,4])

print ("I'm \"ok\".")
print ("I'm learning \nPython.")   # \n 隔行
print ("\\\n\\")
print ("\\ \t \\")
print ('''line1
line 2
line 3''')

True
False

3>2
5>6

5>3 and 3>5
5>3 or 3>5



age = input("Please enter your age: ")
age = int (age)

if age >= 21: 
    print ("Yes, you can.")
else:
    print ("Sorry.")



#Exercise 3
#1.1 = 5
a = 3 
print (a + 2)
#1.2 = 4
a = a + 1.0
print (a)
#1.3 error
#1.4 False , 3
#1.5 True 
#1.6 True 
5/2 == 5/2.0

#2. False, False, True, False

#3. 
import time
raw = time.time()
k = (raw / 60/60/24/365)
year = 1970 + round (k - 0.5)
p = ( k - round (k-0.5) ) * 365  #days


jan = 31
feb = jan + 28
mar = feb +31
apr = mar + 30
may = apr + 31
jun = may + 30
jul = jun + 31
aug = jul + 31
sep = aug + 30 
oct = sep + 31
nov = oct + 30
dec = nov + 31


If year % 4 <> 0:
    if p < (a):
        month = 1
        else:
            if p < (a + m )):
                month = 2
                if p < (a + m )): 
                    month = 2
                    else:
                        if p < (a * 2 + m ):
                            month = 3
                            else:
                                if p < (a * 2 + m + b):
                                    month = 4
                                    else:
                                        if p < (a * 3 + m + b):
                                            month = 5
                                            else:
                                                if p < (a * 3 + m + b * 2):
                                                    month = 6
                                                    else:
                                                        if p < (a * 4 + m + b * 2):
                                                            month = 7
                                                            else:
                                                                if p < (a * 5 + m + b*2):
                                                                    month = 8
                                                                    else:
                                                                        if p < (a * 5 + m + b*3):
                                                                            month = 9
                                                                            else:
                                                                                if p < (a * 6 + m + b*3):
                                                                                    month = 10
                                                                                    else:
                                                                                        if p < (a * 6 + m + b*4):
                                                                                            month = 11
                                                                                            else:
                                                                                                if p < (a * 7 + m + b*4):
                                                                                                    month = 12
                                                                                                    else: 
                                                                                                        print ("error")


else:
b = 29 & if p < (a):
        month = 1
    else:
    if p < (a + m )): 
        month = 2
    else:
    if p < (a * 2 + m ):
        month = 3
    else:
    if p < (a * 2 + m + b):
        month = 4
    else:
    if p < (a * 3 + m + b):
        month = 5
    else:
    if p < (a * 3 + m + b * 2):
        month = 6
    else:
    if p < (a * 4 + m + b * 2):
        month = 7
    else:
    if p < (a * 5 + m + b*2):
        month = 8
    else:
    if p < (a * 5 + m + b*3):
        month = 9
    else:
    if p < (a * 6 + m + b*3):
        month = 10
    else:
    if p < (a * 6 + m + b*4):
        month = 11
    else:
    if p < (a * 7 + m + b*4):
        month = 12
        else: 
            print("error")

date = round (p *365 - month * 30 -0.5)
print (year,month,date)






