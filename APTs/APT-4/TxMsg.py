def getMessage(original):
    """
    return String that is 'textized' version
    of String parameter original
    """

    words = original.split()
    vowels = 'aeiou'
    txt = ''

    for word in words:
        if set(word).intersection(set(vowels)) == set(word):
            txt += word + ' '
        else:
            for i in range(len(word)):
                if word[i] not in vowels:
                    if i == 0 or word[i-1] in vowels:
                        txt += word[i]
            txt += ' '

    return txt.strip() 