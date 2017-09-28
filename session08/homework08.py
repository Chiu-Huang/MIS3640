# team = 'New England Patriots'
# letter = team [1]       # select the 2 nd letter
# # print (letter)      

# print (team [0])
# # print (team [1.5])   Failure


# last = team [len (team)-1]
# print (last)

# last = team [-1]
# print (last)

# # #traversal

# # index = 0 
# # while index < len (team):
# #     letter = team [index]
# #     print (letter)
# #     index += 1

# for letter in team:
#     print (letter)


# prefixes = "JKLMNOPQ"
# suffix = 'ack'
# for letter in prefixes:
#     print (letter+suffix)



# # # Slice : segment of strings
# # team = 'New England Patriots'
# # # print (team[0:11])
# # # print (team [12:])
# # print (team [4:3])   # print out a spacebar
# # print (team [:]) # printing everything 

# # print (team [0:11:2])  #third is step sizes

# team = 'New England Patriots'
# # team[12:20] ='Seahawks'    failure 

# new_team = team [:12] + 'Seahawks'
# print (new_team)




# print (team)


# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1

# print (find(team,"E"))  #return can stop the loop

# word = team
# count = 0
# for k in word:
#     if k == 'a':
#         count += 1
# print (count)              #count how many a's 


# def name_count (string, letter):
#     count = 0
#     for i in string:
#         if string == letter:
#             count += 1
# print (count)



# new_team = team.upper()
# print (new_team) 

# #invocation
# index = team.find ('a')
# print (index)
# print (team.find ('En'))
# print (team.find('a', 10))

# name = 'bob'
# print(name.find('b',1,2))

# print (str.capitalize(name))

# print (str.casefold(name))

# List = ['bananas','rice','paprika','patato chips']





# for i in len (List):
#     k += List[i].split()


# # # for i in len (List):
# #     print (str.split(List[i]))



# # int(ord ()) - 96

# print (len(List))




def any_lowercase1(s):
    if s.islower():
        return True
    else:
        return False

def any_lowercase2(s):
    for c in s:
        if c.islower() == False:
            return False
    return True
            
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
            if flag == false:
                break
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

any_lowercase1('fhwqhdwqijdqwdoi')