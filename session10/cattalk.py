def cons ():
    fin = open ('words.txt')
    for line in fin:
        word = line.strip()
        previous = word[0]
        index = 0
        list1 =[]
        for letter in word:
            if letter == previous:
                index += 1
                previous = letter
                if index == 2:
                    list1 +=[word]
            elif letter != previous:
                previous = letter
                index = 0
        return False

print (cons ())


