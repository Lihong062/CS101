'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: Lihong Wang lw324
'''

import random

def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the 
    corresponding number of misses allowed for the game. 
    '''

    print('How many misses do you want? Hard has 8 and Easy has 12.')
    mode = input('(h)ard or (e)asy> ')

    if mode == 'h':
        return 8
    if mode == 'e':
        return 12

def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''

    wordsoflength = [word for word in words if len(word) == length]
    index = random.randint(0, len(wordsoflength))
    return wordsoflength[index]

def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''

    display = "letters you've guessed:  "
    lettersGuessed = sorted(lettersGuessed)
    for char in lettersGuessed:
        display += char + ' '
    display += '\n'
    display += 'misses remaining = ' + str(missesLeft)
    display += '\n'
    for char in hangmanWord:
        display += char + ' '
    display += '\n'
    return display

def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    
    print(displayString)
    letter = input('letter> ')
    while letter in lettersGuessed:
        print ('you already guessed that')
        letter = input('letter> ')
    return letter

def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    
    for i in range(len(secretWord)):
        if secretWord[i] == guessedLetter:
            hangmanWord[i] = guessedLetter

    return hangmanWord

def processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''

    if guessedLetter not in secretWord: 
    	missesLeft += -1
    updated = updateHangmanWord(guessedLetter, secretWord, hangmanWord)

    return [updated, missesLeft, guessedLetter in secretWord]

def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    
    # Get the word
    words = [word.strip() for word in open(filename).read().split()]
    length = random.randint(5,10)
    secretWord = getWord(words, length)

    # Get the difficulty
    missesLeft = handleUserInputDifficulty()

    # Get the Display
    lettersGuessed = []
    hangmanWord = ['_']*len(secretWord)
    displayString = createDisplayString(lettersGuessed,missesLeft, hangmanWord)

    # Continuing with the game
    while '_' in hangmanWord and missesLeft > 0:
        guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
        gameState = processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft)

        if gameState[2] == True:
            print('you hit: ',guessedLetter, ' in word')
        elif gameState[2] == False:
            print('you missed: ',guessedLetter, ' not in word')

        lettersGuessed.append(guessedLetter)
        lettersGuessed = sorted(lettersGuessed)
        hangmanWord = gameState[0]
        missesLeft = gameState[1]
        displayString = createDisplayString(lettersGuessed,missesLeft, hangmanWord)

        # Ending the game
        if '_' not in hangmanWord:
            print('you guessed the word: ' + secretWord)
            print('you made', len(lettersGuessed),
                  'guesses with', len(set(lettersGuessed) - set(secretWord)),'misses')
            return True
        elif missesLeft == 0:
            print("you're hung!! \nword is " + secretWord)
            print('you made', len(lettersGuessed),
                  'guesses with', len(set(lettersGuessed) - set(secretWord)),'misses')
            return False

if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''

    again = True
    wins = 0
    losses = 0

    while again == True:
        if runGame('lowerwords.txt') == True:
            wins += 1
        else:
            losses += 1
        if input('\nDo you want to play again? y or n> ') == 'n':
            print('Total Wins:', wins)
            print('Total Losses:', losses)
            again = False