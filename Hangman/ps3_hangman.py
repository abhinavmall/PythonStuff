# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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
    s1 = list(set(secretWord))
    s2 = list(set(lettersGuessed))

    s3 = [x for x in s1 if x in s2]

    if len(s3) == len(s1):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    s1 = list(set(lettersGuessed))
    gw = ''

    for c in secretWord:
        if c in lettersGuessed:
            gw+=str(c)
        else:
            gw+=str('_ ')

    return gw


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    s2 = [x for x in string.ascii_lowercase if x not in lettersGuessed]
    return ''.join(s2)

def checkAlreadyGuessed(lettersGuessed, userInput):
    if userInput in lettersGuessed:
        return True
    else:
        return False

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
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')

    guesses = 8
    lettersGuessed = ''
    while(guesses >= 1):
        print('-------------')
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
        print('You have ' + str(guesses) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        userInput = input('Please guess a letter: ')
        # if checkAlreadyGuessed(lettersGuessed, userInput):
        if userInput in lettersGuessed:
            print("Oops! You've already guessed that letter:" + getGuessedWord(secretWord, lettersGuessed))
            continue
        elif userInput not in secretWord:
            lettersGuessed += userInput
            guesses -= 1
            print('Oops! That letter is not in my word:' + getGuessedWord(secretWord, lettersGuessed))
            continue
        elif userInput in secretWord:
            lettersGuessed += userInput
            print('Good guess:' + getGuessedWord(secretWord, lettersGuessed))
            continue

    if guesses == 0 and  not isWordGuessed(secretWord, lettersGuessed):
        print('-----------')
        print('Sorry, you ran out of guesses. The word was ' + secretWord)



# Uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing
# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
