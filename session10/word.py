fin = open ('words.txt')
# fin = open ('words.txt')
# for line in fin:
#     word = line.strip ()
#     print (word)


# fin = open ('words.txt')
# def find_word (x):
#     for line in fin:
#         word = line.strip ()
#         if len(word) > x:
#             print (word)

# find_word (10)


# for letter in word:
#     if letter.lower() =='e':
#         return False
# return True

# def not_ele (s):
#     for line in fin:
#         word = line.strip()
#         return not s in word

# print (not_ele ('e'))

# def not_element (s):
#     for line in fin:
#         word = line.strip ()
#         for letter in word:
#             if letter == s:
#                 break
#         if letter != s:
#             print (word)


# def not_element (s):
#     list1 = []
#     list2 = []
#     for line in fin:
#         word = line.strip ()
#         for letter in word:
#             if letter == s:
#                 break
#         if letter != s:
#             list1 += word
#         else:
#             list2 += word
#     return (len (list1)/(len (list1)+len (list2)))

# not_element ('e')


def percentage (s):
    count1 = 0
    count2 = 0
    k = 0
    for line in fin:
        word = line.strip ()
        for letter in word:
            if letter.lower() == s:
                break
        if letter.lower() != s:
            count1 += 1
        else:
            count2 += 1
    k = ((count1/(count1+count2)))
    print('The percentage of the words with no such letter is {:.2f}%.'.format(k*100))

percentage ('e')



def aviod (word,forbidden):
    fin = open ('words.txt')
    for line in fin:
        words = line.strip ()
        for letter in words:
            if letter in forbidden:
                return False
        return True
print (aviod ('aeiou'))

# not_element ('e')

# def percent 

# def has_no_e(word):
#     return not "e" in word


# def find_words_no_e ():
#     fin = open ('words.txt')
#     for line in fin:
#         word = line.strip ()
#         if has_no_e (word):
#             print (word)





