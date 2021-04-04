
# By Lihong Wang

import os.path
file = os.path.join("data","lowerwords.txt")
f = open(file)
wordsClean = [w.strip() for w in f.read().split()]

shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3]
shifted_upper = upper_alph[3:] + upper_alph[:3]

def setShift(number):
	# set glocal shift, which is used to set the shifted lower and shifted upper strings
    global shift
    shift = number
    global shifted_lower
    shifted_lower = lower_alph[shift:] + lower_alph[:shift]
    global shifted_upper
    shifted_upper = upper_alph[shift:] + upper_alph[:shift]

def encrypt(plaintext):
	# encrypt with a global shit that has been set 
    plaintext = plaintext.split()
    cipertext = []

    for word in plaintext:
    	# loop through each word and add the shifted version to cipertext 
        newWord = ''
        for i in range(len(word)):
            if word[i] in lower_alph:
                newWord += shifted_lower[lower_alph.index(word[i])]
            elif word[i] in upper_alph:
                newWord += shifted_upper[upper_alph.index(word[i])]
            else:
                newWord += word[i]
        cipertext.append(newWord)

    return ' '.join(cipertext)

def findShift(text):
	# Generate a key space with all possible decryptions 
    keySpace = []
    for key in range(26):
        setShift(key)
        keySpace.append(encrypt(text))
    # start an accumulator pattern 
    topMatches = 0
    bestKey = 0
    for i in range(len(keySpace)):
    	# loop through the key space and match the words from elements to the word list 
        counter = 0
        sentence = keySpace[i].split()
        for word in sentence:
            if word in wordsClean:
                counter += 1
        # keep track of the top number of matchs and the best key to ENCRYPT
        if topMatches < counter:
            topMatches = counter
            bestKey = 26 - i 

    return bestKey

if __name__ == '__main__':
	key = findShift('Zkdw grhv wkh ira vdb?')
	print(key)
	setShift(26-key)
	print(encrypt('Zkdw grhv wkh ira vdb?'))