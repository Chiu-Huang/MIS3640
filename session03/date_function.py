import time
raw = time.time()
k = (raw / 60/60/24/365)
year = 1970 + round (k - 0.5)    # how to do yuan nian.. **
yr = (raw / 60 / 60 /24) //365 + 1970 # they are the same thing

def est_time():
    print ("The estimated date is: %4d -%02d -%02d with probably +_ one month. " %(yr,month,day))




p = ( k - round (k-0.5) ) * 365  #days


# assume in a perfect world with no 366 days
rday = raw % 365 //1 
month = rday // 30 
day = rday % 30 //12
 

print('today is %2d -%02d.' % (9,6))
def est_time = :
    print ("The estimated date is: %4d -%02d -%02d with probably +_ one month. " %(yr,month,day))

# probably can try to fix it later