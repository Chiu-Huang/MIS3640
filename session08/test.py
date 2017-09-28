cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0

# while abs(guess**3 -cube) >= epsilon:
#     guess += increment 
#     num_guesses += 1
# print ('number of guesses =', num_guesses)
# if abs(guess**3 - cube) >= epsilon:
#     print ('Failed on cube root of', cube)
# else:
#     print (guess, 'is close to the cube root of', cube)    



def cubic (x):
    epsilon = 0.01
    if abs((x/2) ** 3 - cubic) > epsilon:
        if (x/2) ** 3 < x:
            cubic (x/4)
        else: 
            cubic (3*x/4)
    print (x)