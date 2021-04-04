def check(word):
    """
    return String based on parameter
    word, a String
    """

    for i in range(len(word)):
        try:
            if word[i] not in 'pikachu':
                return 'NO'
            elif word[i] == 'p':
                if word[i+1] != 'i':
                    return 'NO'
            elif word[i] == 'i':
                if word[i-1] != 'p':
                    return 'NO'
            elif word[i] == 'k':
                if word[i+1] != 'a':
                    return 'NO'
            elif word[i] == 'a':
                if word[i-1] != 'k':
                    return 'NO'
            elif word[i] == 'c':
                if word[i+1] != 'h' or word[i+2] != 'u':
                    return 'NO'
            elif word[i] == 'h':
                if word[i+1] != 'u' or word[i-1] != 'c':
                    return 'NO'
            elif word[i] == 'u':
                if word[i-1] != 'h' or word[i-2] != 'c':
                    return 'NO'
        except:
            return 'NO'
    return 'YES'

