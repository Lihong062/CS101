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

def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''

    display = "letters not yet guessed:  "
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in lettersGuessed:
            display += char
        else:
            display += ' '
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

def handleUserInputDebugMode():
    # returns if user wants to play in debug mode
    if input('Which mode do you want: (d)ebug or (p)lay: ') == 'd':
        return True
    else:
        return False

def handleUserInputWordLength():
    # returns the number of letters that the user wants to play with
    return int(input("How many letters in the word you'll guess: "))

def createTemplate(currTemplate, letterGuess, word):
    # helper function (for getNewWordList) to create new template
    currTemplate = list(currTemplate)
    for i in range(len(word)):
        if word[i] == letterGuess:
            currTemplate[i] = letterGuess
    return ''.join(currTemplate)

def getNewWordList(currTemplate, letterGuess, wordList, debug):
    # gets both the new word list and the optimal template
    dict = {}
    for word in wordList:
        newTemplate = createTemplate(currTemplate, letterGuess, word)
        if newTemplate not in dict:
            dict[newTemplate] = [word]
        else:
            dict[newTemplate].append(word)

    dictList = []
    for key, value in dict.items():
        dictList.append([key, value])
    dictList = sorted(dictList, key = lambda x: x[0].count('_'), reverse = True)
    dictList = sorted(dictList, key = lambda x: len(x[1]), reverse = True)

    if debug:
        print()
        for temp in sorted(dictList):
            print(temp[0] + ' : ' + str(len(temp[1])))
        print('# keys = ' + str(len(dictList)))
        print()
        print("# possible words: " + str(len(wordList)))

    return tuple(dictList[0])

def processUserGuessClever(guessedLetter, hangmanWord, missesLeft):
    # processes the user guess
    if guessedLetter in hangmanWord:
        return [missesLeft, True]
    else:
        return [missesLeft - 1, False]

def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''

    # Get the game mode
    debug = handleUserInputDebugMode()

    # Get the words and template
    words = [word.strip() for word in open(filename).read().split()]
    length = handleUserInputWordLength()
    wordList = [word for word in words if len(word) == length]

    # Get the difficulty
    missesLeft = handleUserInputDifficulty()
    print()

    # Get the Display
    lettersGuessed = []
    hangmanWord = ['_']*length
    displayString = createDisplayString(lettersGuessed,missesLeft, hangmanWord)

    # Continuing with the game
    while '_' in hangmanWord and missesLeft > 0:
        guessedLetter = handleUserInputLetterGuess(lettersGuessed, displayString)
        lettersGuessed.append(guessedLetter)


        state = getNewWordList(''.join(hangmanWord),guessedLetter,wordList, debug)
        hangmanWord = list(state[0])
        wordList = state[1]

        if processUserGuessClever(guessedLetter, hangmanWord, missesLeft)[1] == True:
            print('you hit: ', guessedLetter, ' in word')
        else:
            print('you missed: ', guessedLetter, ' not in word')

        missesLeft = processUserGuessClever(guessedLetter, hangmanWord, missesLeft)[0]
        displayString = createDisplayString(lettersGuessed,missesLeft, hangmanWord)

        if debug:
            print("(word is '" + wordList[0] + "')")

        # Ending the game
        if '_' not in hangmanWord:
            print('you guessed the word: ' + wordList[0])
            print('you made', len(lettersGuessed),
                  'guesses with', len(set(lettersGuessed) - set(wordList[0])),'misses')
            return True
        elif missesLeft == 0:
            print("you're hung!! \nword is " + wordList[0])
            print('you made', len(lettersGuessed),
                  'guesses with', len(set(lettersGuessed) - set(wordList[0])),'misses')
            return False

if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''

    again = True
    wins = 0
    losses = 0

    while again == True:
        state = runGame('lowerwords.txt')
        if state == True:
            wins += 1
        if state == False:
            losses += 1
        if input('\nDo you want to play again? y or n> ') == 'n':
            print('Total Wins:', wins)
            print('Total Losses:', losses)
            again = False
