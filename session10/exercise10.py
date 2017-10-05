# fin = open ('texts.txt')



# def uses_only(word, available):
#     for letter in word: 
#         if letter not in available:
#             return False
#     return True


# def uses_all(word, required):
#     return use_only (required, word)


# def is_abecedarian(word):
#     previous = word[0]
#     for c in word:
#         if c < previous:
#             return False
#         previous = c
#     return True

def is_abecedarian(word):
    if len(word) == 1:
        return True
    if word[0] < word [1]:
        is_abecedarian(word[1:])
    else:
        return False

is_abecedarian('abcd')



def is_abecedarian(word):
    i = 1
    while word[i] > word [i-1] and i < len(word):
        i += 1 
    if len (word) == i:
        return True
    else: 
        return False        






