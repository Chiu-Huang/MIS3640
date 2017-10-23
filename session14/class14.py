string.puntucation

        for word in line.split(): # convert strings to list of words
line = line.replace('-',' ')
        strippables = string.punctuation + string.whitespace



        hist[word] = hist.get(word, 0) + 1    # create dictionary


        sorted (dict)  