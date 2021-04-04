def computeSubjects(phrase):
    '''
    Given the string phrase, return a phrase 
    that includes all the words from phrase that do
    not contain a digit or "-" or ":". Those words must
    be in the same order they were in  phrase. 
    '''

    phraseList = phrase.split()
    phrase = ''
    banned = set('1234567890:-')

    for word in phraseList:
        if set(word).intersection(banned) == set():
            phrase += word + ' '
    return phrase.strip()
