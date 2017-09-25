# def sum (n):
#     if n <> 0:
#         return n + sum (n-1)
#     elif n == 0:
#         return 0


 
# def sum (n): 
#     result = 0
#     for i in range (n):
#         result = result + i


# def sum (n):
#     result = 0
#     for i in range (n):
#         result = result + i + 1
#         print ('in the {}th iteration, new result = {}'.format(i,result))

# print (result)



# result = 1

# for i in range (10):
#     result = result * (i+1)
#     print ('in the {}th iteration, new result = {}'.format(i,result))

# print (result)


# #sum of 1000 odds
# result = 0

# for i in range (1,1000,2):
#     result = result + i
#     print ('in the {}th iteration, new result = {}'.format(i,result))

# print (result)


# result = 0

# for i in range (0,1001,2):
#     result = result +i 

# print (result)






# for c in "hello":
#     print (c)


# for alex in ["hello", "world", "babson", "college"]:
#     print (alex)






# #for: know how many iterations, while: when to stop

# def countdown (n):
#     while n > 0:
#         print (n)
#         time.sleep(1)
#         n = n -1
#     print ("Blaseoff!")

# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 


# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 


# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)

# print('Done!')



# mysum = 0
# for i in range(5, 11, 2):
#     mysum += i
#     if mysum == 5:
#         break
# print(mysum)

def sqrt (a):
    x = 1
    y = 0 
    while True:
        y = (x+a/x)/2
        if (x - y) < 0.0001:
            break
    print (y)

sqrt (100)



while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    x = y







