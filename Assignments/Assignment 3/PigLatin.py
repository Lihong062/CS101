
# By Lihong Wang

def hasVowel(text):
    # check if a string contains a vowel
    for char in text:
        if char in 'AEIOUYaeiouy':
            return True
    return False

def isVowelFirst(text):
    # check if the first letter is a vowel 
    return hasVowel(text[0])

def findVowelIndex(text):
    # find the index of the first vowel, from left to right 
    for i in range(len(text)):
        if text[i] in "aeiouyAEIOUY":
            return i

def startWithQU(text):
    # check if a string starts with the letters q and u in that order 
    Q = text[0] == 'q' or text[0] == 'Q'
    U = text[1] == 'u' or text[1] == 'U'
    return Q and U

def findHyphenIndex(text):
    # find the indext of the first hyphen, from right to left 
    for i in reversed(range(len(text))):
        if text[i] == '-':
            return i

def encrypt(plaintext):
    # encrypt a plaintext into pig latin 
    plaintext = plaintext.split()
    cipertext = []

    for word in plaintext:
        if isVowelFirst(word) and word[0] not in 'Yy':
            cipertext.append(word + '-way')
        elif len(word) > 1 and startWithQU(word):
            if hasVowel(word[2:]):
                index = findVowelIndex(word[2:]) + 2
                cipertext.append(word[index:] + '-' + word[:index] + 'ay')
            else:
                cipertext.append(word + '-way')
        elif len(word) > 1 and hasVowel(word[1:]):
            index = findVowelIndex(word[1:]) + 1
            cipertext.append(word[index:] + '-' + word[:index] + 'ay')
        else:
            cipertext.append(word + '-way')

    return ' '.join(cipertext)

def decrypt(ciphertext):
    # decrypts a pig latin text
    ciphertext = ciphertext.split()
    plaintext = []

    for word in ciphertext:
        # if a word end with -way we return the prefix 
        if word[-4:] == '-way':
            plaintext.append(word[:-4])
        else:
            index = findHyphenIndex(word)
            plaintext.append(word[index+1:-2] + word[:index])

    return ' '.join(plaintext)

if __name__ == '__main__':
    print(encrypt('The quiz was easy once I got into the rhythm'))