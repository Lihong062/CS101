def getStats(sentence):
    '''
    sentence (str) - a string with a potential pangram in it

    For all the letters return a list where value at the kth index is the
    number of letters that occur k times.
    '''

    sentence = sentence.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    max = 0
    for char in alpha:
        if sentence.count(char) > max:
            max = sentence.lower().count(char)

    ret = [0]*(max+1)
    for char in alpha:
        index = sentence.count(char)
        ret[index] += 1

    return ret

