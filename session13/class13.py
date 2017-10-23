# d = {'a' : 120, 'b': 130, 'b': 130}

# cheating, game action = enter, input
# if input() = 


# set([1,2,3,4,5,5])


# d.value()


# True + True
# True + False



email = 'zli@babson.edu'
id, domain = email.split('@')
print(id)
print(domain)

t = divmod(7, 3) # divide and remainder
print(t)

def printall(*args):
    print(args)




def sumall (*args):
    return len(args)     


s = 'abc'
t = [0, 1, 2]
zip(s, t)

for pair in zip(s, t):
    print(pair)


# def most_frequent (string):
    

def anagrams():
    d ={}
    fin = open('words.txt')
    for word in fin:
        word = word.strip()
        hlist = []
        for element in word:
           hlist += element
        d[word] = hlist
    return d



print(anagrams())
