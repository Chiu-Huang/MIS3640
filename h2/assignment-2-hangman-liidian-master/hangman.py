# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random, string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
# When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# lettersGuessed = ['a', 'p', 'l', 'r', 'e', 's']
# print(isWordGuessed(secretWord, lettersGuessed))

# Expected output:
# False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessword = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessword +='_'
        if letter in lettersGuessed:
            guessword += letter  
    return guessword

# When you've completed your function getGuessedWord, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))

# Expected output:
# '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.

    # FILL IN YOUR CODE HERE...
    available = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            available += letter
    return available 
# When you've completed your function getAvailableLetters, uncomment these two lines
# and run this file to test!

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))

# Expected output:
# abcdfghjlmnoqtuvwxyz


def playagain():
    p = input ("Playagain? Y/N")
    if p.lower() == 'y':
        secretWord = chooseWord(wordlist).lower()
        hangman(secretWord)
    else:
        exit()

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    nguess = 8
    lettersGuessed =[]
    display = getGuessedWord(secretWord, lettersGuessed)
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    print ('---------------------------------------------')
    while nguess > 0: 
        print ("You have {} guesses left".format(nguess))
        print ('Available Letters: {}'.format(getAvailableLetters(lettersGuessed)))
        t = input("Please guess a letter: ")
        if t in lettersGuessed:
            print ("Oops! You've already guessed that letter: {}".format(display))
        elif len(t) != 1:
            print ("Oops! You've typed more than 1 letters: {}".format(display)) 
        elif t not in string.ascii_lowercase:
            print ("Opps! You've typed something that is not a letter: {}".format(display))
        elif t in secretWord:
            lettersGuessed += t
            display = getGuessedWord(secretWord, lettersGuessed)
            print ("Good guess: {}".format(display))
        else: 
            lettersGuessed += t
            display = getGuessedWord(secretWord, lettersGuessed)
            print ("Oops! That letter is not in my word: {}".format(display))
            nguess -= 1
        print ('---------------------------------------------')
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Congratulations, you won! The word is {}".format(secretWord))
            return playagain()
    print ("Sorry, you ran out of guesses. The word was {}".format(secretWord))
    return playagain()
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
