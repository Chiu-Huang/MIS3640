def sleep_in(weekday, vacation):
      if weekday == False or vacation == True:
    return True 
  else:
    return False



def diff21(n):
      if n > 21:
    return 2 * abs (21-n)
  else:
    return abs (21-n)

def near_hundred(n):
      if  ( abs (n-100) <= 10  or abs (n -200) <= 10): 
    return True 
  else:
    return False

