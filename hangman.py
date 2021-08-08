# Hangman game

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
    r=random.choice(wordlist)
    while(len(r)>7):
        r=random.choice(wordlist)
    return r


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
    
    found=False
    for a in secretWord:
        if(a not in lettersGuessed):
            found=False
            break
        else:  
             found=True
    return found      



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    found=''
    for a in secretWord:
        if(a in lettersGuessed):
              found=found+a
        else:  
              found=found+'_'
    return found  


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    remaining=''
    for a in string.ascii_lowercase:
        if(a not in lettersGuessed):
            remaining=remaining+a
    return remaining

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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord),"letters long")
    print("-------------")
    lettersGuessed=[]
    for i in range (0,8):
        print("You have",8-i,"guesses left")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        Guess=input("Please guess a letter:")
        g= Guess.lower()
        if(g in lettersGuessed):
           print("Oops! You've already guessed that letter:",s)
           print("------------")
           
        else:
            lettersGuessed +=g
            s=getGuessedWord(secretWord, lettersGuessed)
            if( g in secretWord):
                i-=1
                print("Good guess:",s)
                print("------------")
                if(isWordGuessed(secretWord, lettersGuessed)):
                   print("Congratulations, you won!")
                   break
            else:
                print("Oops! That letter is not in my word:",s)
                print("------------")
    print("Sorry, you ran out of guesses. The word was",secretWord,".")

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
