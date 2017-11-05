from datetime import *

def calendarmonth():
    k = date.today()

    if (date.isoweekday(k)) == 1:
        p = ("Monday")
    elif (date.isoweekday(k)) == 2:
        p = ("Tuesday")
    elif (date.isoweekday(k)) == 3:
        p = ("Wednesday")
    elif (date.isoweekday(k)) == 4:
        p = ("Thursday")
    elif (date.isoweekday(k)) == 5:
        p = ("Friday")
    elif (date.isoweekday(k)) == 6:
        p = ("Saturday")
    elif (date.isoweekday(k)) == 7:
        p = ("Sunday")

    print ('Today is {} and it\'s {}.'.format(k,p))

calendarmonth()

# ts the current date and prints the day of the week.

#raise 