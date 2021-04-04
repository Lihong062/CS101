def countVowelWords(phrase):
    '''
    Given a string parameter
    phrase, return the number of words 
    in phrase that start with and end with 
    a different vowel. 
    '''

    phraseList = phrase.split()
    vowels = 'aeiouAEIOU'
    counter = 0

    for phrase in phraseList:
        if phrase[0] in vowels and phrase[-1] in vowels and phrase[0] != phrase[-1]:
            counter += 1

    return counter

