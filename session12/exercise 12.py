#Exercise 1
def histogram(s):
    d = dict()
    for letter in s.lower():
        d[letter] = d.get(letter, 0) + 1
    return d

#Exercise 2
def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


known = {1: 1, 2: 2}


def fib_efficient(n):
    global numFibCalls
    numFibCalls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


numFibCalls = 0
fibArg = 10

print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0


print(fib_efficient(fibArg))
print('function calls', numFibCalls)



#3
# Global Variables are Known and numFibCalls. NumfibCalls is global so that the value can be updated each time when it goes through the function. The functions are different
# because known is used to store data, versus numfibcalls is the x-input that changes.

#4 
def dictword ():
    fin = open ('words.txt')
    wordd = {}
    count = 0
    for word in fin:
        word = word.strip ()
        count += 1
        wordd [word] = count
    return wordd
print(dictword())


def has_duplicates (list1):
    while len(list1) > 1:
        if list1[0] in list1[1:]:
            return True
        else:
            list1.pop(0)
            has_duplicates (list1)
    return False
q= [1,2,3,4]
has_duplicates (q)




