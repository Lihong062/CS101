def check(phrase, let1, let2):
    '''
    phrase is a string of words, let1
    and let2 are both strings of a single
    letter.

    Returns in sorted order, a String
    of the words from phrase that
    that have both let1 and let2 in them,
    each at least once, but do not have the
    two letters adjacent.
    '''

    phrase = phrase.split()
    ret = []

    if let1 != let2:
        for word in phrase:
            if let1 in word and let2 in word:
                ret.append(word)
            for i in range(len(word)-1):
                if let1 in [word[i],word[i+1]] and let2 in [word[i],word[i+1]]:
                    try:
                        ret.remove(word)
                    except:
                        pass
    elif let1 == let2:
        for word in phrase:
            if word.count(let1) >= 2:
                ret.append(word)
            for i in range(len(word)-1):
                if [let1,let1] == [word[i],word[i+1]]:
                    try:
                        ret.remove(word)
                    except:
                        pass

    return ' '.join(sorted(ret))
