AFC_east = ['New England Patriots', "Buffalo Bills", "Miami Dolphins", "New York Jets"]
numbers = [42,123]
empty = []

AFC_east[3] = 'New York Giants'

print (AFC_east)



AFC_east[-1]

print ('Buffalo Bills' in AFC_east)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

print (L[0][0])
print (L[-1][-1])
print (L[1][2][1])


for team in AFC_east:
    print (team)
numbers = [2, 0, 1, 6, 9]

for i in range (len(numbers)):
    numbers[i] = numbers[i] * 2

print (numbers)



new_numbers = [number * 2  for number in numbers]
print (new_numbers)

my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))
print (len (my_list[2]))


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)



print ([0] * 4)

t = ['a', 'b', 'c', 'd', 'e', 'f']

t[1:3] = ['x', 'y']
print(t)

t[-3:]

# import numpy as np
# a = np.array (a)
# b= np.array (b)
# a * b


a.append ('g')

a.extend (b)

a.insert (2, "Winfred")  #define location

a.remove ('Winfred')

v = [1,2,3,45,6665,4,21323,24,51,32134]
v.sort

AFC_east.sort()

AFC_west = AFC_east.copy() # lists change together 




