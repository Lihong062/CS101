def acronym(phrase):
    """
    phrase is a string, zero or more spaces
    return a string: acronym of the string
    parameter phrase
    """

    shortened = ''
    split = phrase.split()
    for word in split:
        shortened += word[0]
    return shortened
