import random
import csv

x = int(input('Enter an integer: '))
ans = 0
if x > 0:
    while ans**3 < x:
        ans = ans + 1
else:
    while ans**3 > x:
        ans = ans - 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))




cube = -28
for guess in range (abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess == abs (cube):
    print(str(cube) + " is a cube of " + str(guess))
else:
    print (str(cube) + " is not a perfect cube")









cube = 29
epsilon = 0.01
guess = 0.0
increment = 0.005
num_guesses = 0

while abs(guess**3 -cube) >= epsilon:
    guess += increment 
    num_guesses += 1
print ('number of guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print ('Failed on cube root of', cube)
else:
    print (guess, 'is close to the cube root of', cube)    
