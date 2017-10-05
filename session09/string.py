team = 'New England Patriots'

letter = team [0]

# # print (team[-2])
# # print (team[-1])
# # print (team [len(team)-1])

# for i in team:
#     if i != " ":
#         print (i)

# for i in team:
#     if i.isalpha():
#         print (i)

# for i in range (len(team)):
#     if team [i] != ' ':
#         print (team[i])

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter != 'O' and letter != 'Q':
#         print(letter + suffix)
#     else:
#         print (letter +'u'+ suffix)

# for letter in prefixes:
#     if letter in 'OQ':
#         print (letter + 'u'+ suffix)
#     else:
#         print (letter + suffix)

# for letter in prefixes:
#     if letter in ['O','Q']:
#         letter = letter + 'u'
#     print (letter + suffix)


def count (y, x):
    count = 0
    for i in y:
        if i == 'x':
            count +=1
    return (count)

def vcount (y):
    count = 0
    for i in y:
        if i in 'aeiouAEIOU':
            count += 1
    return count



def vvcount (y):
    vowel = 'aeiou'
    k = 0
    for i in vowel:
        k += count (y,i)
    return (k)


def count (word, letter):
    count = 0
    word = word.lower()
    letter = letter.lower()
    for i in word:
        if i == letter:
            count += 1
    return count



#pyformat