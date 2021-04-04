def countwords(phrase, ending, item):
    '''
    Given the three string parameters 
    phrase, ending and item, 
    return the number of words in phrase 
    that end in ending and do not contain
    item as part of their word.
    '''
    counter = 0
    phraseList = phrase.split()
    for word in phraseList:
        if item not in word:
            if len(word) >= len(ending):
                l = len(ending)
                if word[-l:] == ending:
                    counter += 1
    return counter
