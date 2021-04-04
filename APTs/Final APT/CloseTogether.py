def compute(phrase):
    '''
    phrase is a string of words

    Returns in sorted order, a String
    of the unique words from phrase that
    that have the smallest "closeness"
    '''

    phrase = phrase.split()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    closeness = []
    ret = []

    for word in phrase:
        distance = []
        for char1 in word:
            for char2 in word:
                dist = abs(alpha.index(char1)-alpha.index(char2))
                distance.append(dist)
        closeness.append(max(distance))

    for i in range(len(closeness)):
        if closeness[i] == (min(closeness)):
            ret.append(phrase[i])

    return ' '.join(sorted(set(ret)))
