def compute(phrase, one, two, sep):
    '''
    Given the four string parameters 
    phrase, one, two and sep, 
    return a string of the decoded
    message. 
    '''

    phraseList = phrase.split()
    decoded = ''
    for word in phraseList:
        if word[0] == one:
            decoded += word[-1]
        elif two in word and len(word)>2:
            decoded += word[2]
        elif word[0] == sep or word[-1] == sep:
            decoded += '-'
    return decoded
